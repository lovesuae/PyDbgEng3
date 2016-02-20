#! /user/bin/python
# coding:UTF-8

from multiprocessing import *

from PyDbgEng3.DbgEventHandler import *

from PyDbgEng3.PyDbgEng.ProcessCreator import ProcessCreator

# you can set log file path to trace parameter
# or it will be return exception string when tarce is none
def Run(cmd, trace=None):

    p = os.path.dirname(__file__) + "/PyDbgEng/DbgEngDll/"
    if sys.version.find("AMD64") != -1:
        p += "x64"
    else:
        p += "x86"

    started = Event()
    CommandLine = cmd
    SymbolsPath = b"SRV*http://msdl.microsoft.com/download/symbols"
    DbgEngDllPath = p
    HandlingFault = Event()
    HandledFault = Event()
    IgnoreFirstChanceGardPage = False
    IgnoreSecondChanceGardPage = False
    quit = Event()
    FaultOnEarlyExit = False

    dbg = None

    # Hack for comtypes early version
    comtypes._ole32.CoInitializeEx(None, comtypes.COINIT_APARTMENTTHREADED)

    try:
        _eventHandler = DbgEventHandler()
        _eventHandler.pid = None
        _eventHandler.handlingFault = HandlingFault
        _eventHandler.handledFault = HandledFault
        _eventHandler.IgnoreFirstChanceGardPage = IgnoreFirstChanceGardPage
        _eventHandler.IgnoreSecondChanceGardPage = IgnoreSecondChanceGardPage
        _eventHandler.quit = quit
        _eventHandler.Tempfile = trace
        _eventHandler.FaultOnEarlyExit = FaultOnEarlyExit

        dbg = ProcessCreator(command_line = CommandLine,
            follow_forks = True,
            event_callbacks_sink = _eventHandler,
            output_callbacks_sink = _eventHandler,
            symbols_path = SymbolsPath,
            dbg_eng_dll_path = DbgEngDllPath)

        _eventHandler.dbg = dbg
        started.set()
        dbg.event_loop_with_quit_event(quit)
    except Exception as e:
        print(e)
    return _eventHandler.crashInfo