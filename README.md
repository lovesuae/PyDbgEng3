### PyDbgEng3

PyDbgEng is a python compact wrapper from PyDbgEng for microsoft debug engine.

### Features

* The automated monitoring module specially developed for Fuzzing
* Using dbgeng.dll and dbghelp.dll of the house
* Supports !Exploitable plug-ins MSEC.dll which is v1.6.0

### Requirements

* Required
    * Python >= 3.0

### Usages

	from PyDbgEng3 import Debugger
	proc_args = b"C:/Program Files/Internet Explorer/iexplore.exe"
	crashInfo = Debugger.Run(proc_args)

When the target process loaded using proc_args is crahsed, You can get crashInfo['bucket']like this:

	PROBABLY_NOT_EXPLOITABLE_ReadAVNearNull_0x76da4b51_0x429cabbb

and crashInfo['description'] like this:

	INSTRUCTION_ADDRESS:0x000007fabd1c96e1
	INVOKING_STACK_FRAME:0
	DESCRIPTION:Read Access Violation near NULL
	SHORT_DESCRIPTION:ReadAVNearNull
	CLASSIFICATION:PROBABLY_NOT_EXPLOITABLE
	BUG_TITLE:Read Access Violation near NULL starting at MSHTML!DllCanUnloadNow+0x01 (Hash=0x76da4b51.0x429cabbb)
	EXPLANATION:This is a user mode read access violation near null, and is probably not exploitable.

### Versions
	
Currently only to v0.0.1.

------

If you have any bug or suggestions, please e-mail contact walkerfuz#outlook.com.
