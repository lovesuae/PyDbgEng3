#! /user/bin/python
# coding:UTF-8

from setuptools import setup, find_packages
setup(
    name='PyDbgEng3',
    version="0.0.2",
    description='A Python Wrapper For Microsoft Debug Engine',
    author='Walkerfuz',
    author_email='walkerfuz#outlook.com',
    url='https://github.com/walkerfuz/PyDbgEng3',
    package_dir={
        'PyDbgEng3': '.',
        'PyDbgEng3.PyDbgEng': 'PyDbgEng',
		'PyDbgEng3.PyDbgEng.DbgEngDll': 'PyDbgEng/DbgEngDll',
		'PyDbgEng3.PyDbgEng.DbgEngDll.x64': 'PyDbgEng/DbgEngDll/x64',
		'PyDbgEng3.PyDbgEng.DbgEngDll.x86': 'PyDbgEng/DbgEngDll/x86',
		'PyDbgEng3.PyDbgEng.Exploitable': 'PyDbgEng/Exploitable',
		'PyDbgEng3.PyDbgEng.Exploitable.x64': 'PyDbgEng/Exploitable/x64',
		'PyDbgEng3.PyDbgEng.Exploitable.x86': 'PyDbgEng/Exploitable/x86',
		'PyDbgEng3.PyDbgEng.Data': 'PyDbgEng/Data',
    },
    packages=['PyDbgEng3',
                 'PyDbgEng3.PyDbgEng',
                 'PyDbgEng3.PyDbgEng.DbgEngDll',
                 'PyDbgEng3.PyDbgEng.DbgEngDll.x64',
                 'PyDbgEng3.PyDbgEng.DbgEngDll.x86',
                 'PyDbgEng3.PyDbgEng.Exploitable',
                 'PyDbgEng3.PyDbgEng.Exploitable.x64',
                 'PyDbgEng3.PyDbgEng.Exploitable.x86',
				 'PyDbgEng3.PyDbgEng.Data',
	],
    package_data={
        'PyDbgEng3.PyDbgEng.DbgEngDll.x64': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.DbgEngDll.x86': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.Exploitable.x64': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.Exploitable.x86': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.Data': ['*.tlb', ],
    },
    data_files=[
		('PyDbgEng3/PyDbgEng/DbgEngDll/x64', ['PyDbgEng/DbgEngDll/x64/dbgeng.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x64', ['PyDbgEng/DbgEngDll/x64/dbghelp.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x86', ['PyDbgEng/DbgEngDll/x86/dbgeng.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x86', ['PyDbgEng/DbgEngDll/x86/dbghelp.dll']),
		('PyDbgEng3/PyDbgEng/Exploitable/x64', ['PyDbgEng/Exploitable/x64/MSEC.dll']),
		('PyDbgEng3/PyDbgEng/Exploitable/x86', ['PyDbgEng/Exploitable/x86/MSEC.dll']),
		('PyDbgEng3/PyDbgEng/Data', ['PyDbgEng/Data/DbgEng.tlb']),
	],
    include_package_data=True,	
	
)
