#! /user/bin/python
# coding:UTF-8

class Monitor:
	'''
	Extend from this to implement a Monitor.  Monitors are
	run by an Agent and must operate in an async mannor.  Any
	blocking tasks must be performed in another thread.
	'''

	def __init__(self, args):
		'''
		Constructor.  Arguments are supplied via the Peach XML
		file.

		@type	args: Dictionary
		@param	args: Dictionary of parameters
		'''

		# Our name for this monitor
		self._name = None

	def OnTestStarting(self):
		'''
		Called right before start of test case or variation
		'''
		pass

	def OnTestFinished(self):
		'''
		Called right after a test case or varation
		'''
		pass

	def GetMonitorData(self):
		'''
		Get any monitored data from a test case.
		'''
		return None

	def RedoTest(self):
		'''
		Should the current test be reperformed.
		'''
		return False

	def DetectedFault(self):
		'''
		Check if a fault was detected.
		'''
		return False

	def OnFault(self):
		'''
		Called when a fault was detected.
		'''
		pass

	def OnShutdown(self):
		'''
		Called when Agent is shutting down, typically at end
		of a test run or when a Stop-Run occurs
		'''
		pass

	def StopRun(self):
		'''
		Return True to force test run to fail.  This
		should return True if an unrecoverable error
		occurs.
		'''
		return False

	def PublisherCall(self, method):
		'''
		Called when a call action is being performed.  Call
		actions are used to launch programs, this gives the
		monitor a chance to determin if it should be running
		the program under a debugger instead.

		Note: This is a bit of a hack to get this working
		'''
		pass