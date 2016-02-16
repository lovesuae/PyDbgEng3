#! /user/bin/python
# coding:UTF-8

from setuptools import setup, find_packages
setup(
    name='PyDbgEng3',
    version="0.0.1",
    description='A Python Wrapper For Microsoft Debug Engine',
    author='Walkerfuz',
    author_email='walkerfuz#outlook.com',
    url='https://github.com/walkerfuz/PyDbgEng3',
    package_dir={
        'PyDbgEng3': 'source',
        'PyDbgEng3.PyDbgEng': 'source/PyDbgEng',
		'PyDbgEng3.PyDbgEng.DbgEngDll': 'source/PyDbgEng/DbgEngDll',
		'PyDbgEng3.PyDbgEng.DbgEngDll.x64': 'source/PyDbgEng/DbgEngDll/x64',
		'PyDbgEng3.PyDbgEng.DbgEngDll.x86': 'source/PyDbgEng/DbgEngDll/x86',
		'PyDbgEng3.PyDbgEng.Exploitable': 'source/PyDbgEng/Exploitable',
		'PyDbgEng3.PyDbgEng.Exploitable.x64': 'source/PyDbgEng/Exploitable/x64',
		'PyDbgEng3.PyDbgEng.Exploitable.x86': 'source/PyDbgEng/Exploitable/x86',
    },
    packages=['PyDbgEng3',
                 'PyDbgEng3.PyDbgEng',
                 'PyDbgEng3.PyDbgEng.DbgEngDll',
                 'PyDbgEng3.PyDbgEng.DbgEngDll.x64',
                 'PyDbgEng3.PyDbgEng.DbgEngDll.x86',
                 'PyDbgEng3.PyDbgEng.Exploitable',
                 'PyDbgEng3.PyDbgEng.Exploitable.x64',
                 'PyDbgEng3.PyDbgEng.Exploitable.x86',
	],
    package_data={
        'PyDbgEng3.PyDbgEng.DbgEngDll.x64': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.DbgEngDll.x86': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.Exploitable.x64': ['*.dll', ],
		'PyDbgEng3.PyDbgEng.Exploitable.x86': ['*.dll', ],
    },
    data_files=[
		('PyDbgEng3/PyDbgEng/DbgEngDll/x64', ['source/PyDbgEng/DbgEngDll/x64/dbgeng.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x64', ['source/PyDbgEng/DbgEngDll/x64/dbghelp.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x86', ['source/PyDbgEng/DbgEngDll/x86/dbgeng.dll']),
		('PyDbgEng3/PyDbgEng/DbgEngDll/x86', ['source/PyDbgEng/DbgEngDll/x86/dbghelp.dll']),
		('PyDbgEng3/PyDbgEng/Exploitable/x64', ['source/PyDbgEng/Exploitable/x64/MSEC.dll']),
		('PyDbgEng3/PyDbgEng/Exploitable/x86', ['source/PyDbgEng/Exploitable/x86/MSEC.dll']),
	],
    include_package_data=True,	
	
)
