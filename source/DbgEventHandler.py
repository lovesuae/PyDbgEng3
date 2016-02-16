#! /user/bin/python
# coding:UTF-8

import os
import sys
import re
import pickle
from ctypes import *
import comtypes
from comtypes.gen import DbgEng
import hashlib
import psutil

from .PyDbgEng.PyDbgEng import IDebugOutputCallbacksSink
from .PyDbgEng.PyDbgEng import IDebugEventCallbacksSink

class DbgEventHandler(IDebugOutputCallbacksSink, IDebugEventCallbacksSink):

    buff = ''
    TakeStackTrace = True
    crashInfo = None

    def Output(self, this, Mask, Text):
        try:
            self.buff += Text.decode()
        except:
            pass

    def GetInterestMask(self):
        #	return PyDbgEng.DbgEng.DEBUG_EVENT_EXCEPTION | PyDbgEng.DbgEng.DEBUG_FILTER_INITIAL_BREAKPOINT | \
	    #	       PyDbgEng.DbgEng.DEBUG_EVENT_EXIT_PROCESS | PyDbgEng.DbgEng.DEBUG_EVENT_LOAD_MODULE
        return DbgEng.DEBUG_EVENT_EXCEPTION | DbgEng.DEBUG_FILTER_INITIAL_BREAKPOINT | DbgEng.DEBUG_EVENT_LOAD_MODULE

    def LoadModule(self, dbg, ImageFileHandle, BaseOffset, ModuleSize, ModuleName, ImageName, CheckSum, TimeDateStamp):
        return DbgEng.DEBUG_STATUS_NO_CHANGE

    def ExitProcess(self, dbg, ExitCode):
        self.quit.set()
        return DbgEng.DEBUG_STATUS_NO_CHANGE

    def Exception(self, dbg, ExceptionCode, ExceptionFlags, ExceptionRecord,
            ExceptionAddress, NumberParameters, ExceptionInformation0, ExceptionInformation1,
            ExceptionInformation2, ExceptionInformation3, ExceptionInformation4,
            ExceptionInformation5, ExceptionInformation6, ExceptionInformation7,
            ExceptionInformation8, ExceptionInformation9, ExceptionInformation10,
            ExceptionInformation11, ExceptionInformation12, ExceptionInformation13,
            ExceptionInformation14, FirstChance):

        if self.IgnoreSecondChanceGardPage and ExceptionCode == 0x80000001:
            return DbgEng.DEBUG_STATUS_NO_CHANGE

        # Only capture dangerouse first chance exceptions
        if FirstChance:
            if self.IgnoreFirstChanceGardPage and ExceptionCode == 0x80000001:
                # Ignore, sometimes used as anti-debugger
                # by Adobe Flash.
                return DbgEng.DEBUG_STATUS_NO_CHANGE

            # Guard page or illegal op
            elif ExceptionCode == 0x80000001 or ExceptionCode == 0xC000001D:
                pass
            elif ExceptionCode == 0xC0000005:
                # is av on eip?
                if ExceptionInformation0 == 0 and ExceptionInformation1 == ExceptionAddress:
                    pass

                # is write a/v?
                elif ExceptionInformation0 == 1 and ExceptionInformation1 != 0:
                    pass

                # is DEP?
                elif ExceptionInformation0 == 0:
                    pass

                else:
                    # Otherwise skip first chance
                    return DbgEng.DEBUG_STATUS_NO_CHANGE
            else:
                # otherwise skip first chance
                return DbgEng.DEBUG_STATUS_NO_CHANGE


        if self.handlingFault.is_set() or self.handledFault.is_set():
            # We are already handling, so skip
            return DbgEng.DEBUG_STATUS_BREAK

        try:
            # print("DbgEventHandler:ExceptionCode=0x%X, ExceptionAddress=0x%X." % (ExceptionCode, ExceptionAddress))
            self.buff = ''
            self.crashInfo = {}
            self.handlingFault.set()

            if self.pid == None:
                dbg.idebug_control.Execute(DbgEng.DEBUG_OUTCTL_THIS_CLIENT,
                                                c_char_p(b"|."),
                                                DbgEng.DEBUG_EXECUTE_ECHO)
                match = re.search(r"\.\s+\d+\s+id:\s+([0-9a-fA-F]+)\s+\w+\s+name:\s", self.buff)
                if match != None:
                    self.pid = int(match.group(1), 16)

            ## 1. Output registers
            dbg.idebug_control.Execute(DbgEng.DEBUG_OUTCTL_THIS_CLIENT,
                                       c_char_p(b"r"),
                                       DbgEng.DEBUG_EXECUTE_ECHO)
            self.buff += "\n"

            ## 2. Ouput stack trace
            if DbgEventHandler.TakeStackTrace:
                #print("Exception: 2. Output stack trace")

                dbg.idebug_control.Execute(DbgEng.DEBUG_OUTCTL_THIS_CLIENT,
                                           c_char_p(b"k"),
                                           DbgEng.DEBUG_EXECUTE_ECHO)
                self.buff += "\n"

            else:
                DbgEventHandler.TakeStackTrace = True
                self.buff += "\n[Exception] Error, stack trace failed.\n"

            ## 3. Write dump file
            minidump = None

            ## 4. Bang-Exploitable
            try:
                p = os.path.dirname(__file__) + "/PyDbgEng/Exploitable/"
                if sys.version.find("AMD64") != -1:
                    p += "x64"
                else:
                    p += "x86"

                p = ".load %s\\MSEC.dll" % p

                dbg.idebug_control.Execute(DbgEng.DEBUG_OUTCTL_THIS_CLIENT, c_char_p(p.encode(encoding="utf-8")), DbgEng.DEBUG_EXECUTE_ECHO)
                dbg.idebug_control.Execute(DbgEng.DEBUG_OUTCTL_THIS_CLIENT, c_char_p(b"!exploitable -m"), DbgEng.DEBUG_EXECUTE_ECHO)
            except:
                raise

            ## Do we have !exploitable?
            try:
                majorHash = re.compile("^MAJOR_HASH:(0x.*)$", re.M).search(self.buff).group(1)
                minorHash = re.compile("^MINOR_HASH:(0x.*)$", re.M).search(self.buff).group(1)
                classification = re.compile("^CLASSIFICATION:(.*)$", re.M).search(self.buff).group(1)
                shortDescription = re.compile("^SHORT_DESCRIPTION:(.*)$", re.M).search(self.buff).group(1)
                if majorHash != None and minorHash != None:
                    bucket = "%s_%s_%s_%s" % (classification, shortDescription, majorHash, minorHash)
            except:
                x = (ExceptionCode, ExceptionFlags, ExceptionRecord,
                        ExceptionAddress, NumberParameters, ExceptionInformation0, ExceptionInformation1,
                        ExceptionInformation2, ExceptionInformation3, ExceptionInformation4,
                        ExceptionInformation5, ExceptionInformation6, ExceptionInformation7,
                        ExceptionInformation8, ExceptionInformation9, ExceptionInformation10,
                        ExceptionInformation11, ExceptionInformation12, ExceptionInformation13,
                        ExceptionInformation14, FirstChance)
                h = hashlib.md5()
                h.update((''.join([str(item) for item in list(x)])).encode(encoding='utf-8'))
                bucket = "Unknown_%s" % (h.hexdigest())
            # Done

        except Exception as e:
            print(e)
            raise

        if self.Tempfile is not None:
            try:
                #print "Exception: Writing to file"
                fd = open(self.Tempfile + "/" + bucket + '.crash' , "w")
                fd.write(self.buff)
                fd.close()
            except Exception as e:
                print(e)
                raise
        else:
            pass

        self.crashInfo['bucket'] = bucket
        self.crashInfo['description'] = self.buff

        self.buff = ""
        self.fault = True

        if self.pid != None:
            psutil.Process(self.pid).terminate()

        self.handledFault.set()
        return DbgEng.DEBUG_STATUS_GO