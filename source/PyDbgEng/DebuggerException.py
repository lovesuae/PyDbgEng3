#! /user/bin/python
# coding:UTF-8

###########################################################
class DebuggerException(Exception):
    message = None
    
    ###########################################################
    def __init__(self, message):
        self.message = message
        
    ###########################################################
    def __str__(self):
        return self.message