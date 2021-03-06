# About

PyDbgEng is a python compact wrapper from PyDbgEng for microsoft debug engine.

# Features

* The automated monitoring module specially developed for Fuzzing
* Using dbgeng.dll and dbghelp.dll of the house
* Supports !Exploitable plug-ins MSEC.dll which is v1.6.0

# Requirements

* Required
    * Python >= 3.0
	* psutil
	* comtypes
	* Visual C++ Redistributable 2012

# Install

Download psutil from https://pypi.python.org/pypi/psutil and setup.

Download comtypes from https://github.com/enthought/comtypes and setup.

Download Visual C++ Redistributable 2012 from https://www.microsoft.com/en-us/download/details.aspx?id=30679 and setup.

Download PyDbgEng3 from https://github.com/walkerfuz/PyDbgEng3 adn setup.
	
# Usages

	from PyDbgEng3 import Debugger
	proc_args = b"C:/Program Files/Internet Explorer/iexplore.exe"
	crashInfo = Debugger.Run(proc_args, minorHash=True, mode="M"/"S", trace=None)

1. If set minorHash is True, you will get crashInfo['bucket']like this:

> PROBABLY_NOT_EXPLOITABLE_ReadAVNearNull_0x76da4b51_0x429cabbb
	
and if set minorHash is False, you will get crashInfo['bucket']like this:

> PROBABLY_NOT_EXPLOITABLE_ReadAVNearNull_0x76da4b51


2. When target process is multiprocess like chrome and IEx64, you should set mode to 'M' which is equal to Multiprocess, and 
when target process is singleprocess like firefox, you should set mode to 'S' whick is equal to Singleprocess.

3. You can set trace to one folder to save crash info which name like this:

> PROBABLY_NOT_EXPLOITABLE_ReadAVNearNull_0x76da4b51.crash

4. crashInfo['description which is in crash file like this:

	INSTRUCTION_ADDRESS:0x000007fabd1c96e1
	INVOKING_STACK_FRAME:0
	DESCRIPTION:Read Access Violation near NULL
	SHORT_DESCRIPTION:ReadAVNearNull
	CLASSIFICATION:PROBABLY_NOT_EXPLOITABLE
	BUG_TITLE:Read Access Violation near NULL starting at MSHTML!DllCanUnloadNow+0x01 (Hash=0x76da4b51.0x429cabbb)
	EXPLANATION:This is a user mode read access violation near null, and is probably not exploitable.

# Versions

* v0.0.3
	* fix bugs when process is singleprocess or multiprocess.
* v0.0.2
	* fix bugs when comtypes.gen isn't exist.
	* add Visual C++ Redistributable 2012 setup to install steps.
* v0.0.1
	* change pydbgeng for python 3.x.

------

If you have any bug or suggestions, please e-mail contact walkerfuz#outlook.com.
