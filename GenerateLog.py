#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from importlib import reload
import datetime
import sys,os
import rospy
import logging
from rosgraph.roslogging import RosStreamHandler as RosStreamHandler



class logHandling:
    def __init__(self):
        self.log=logging
        #sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './src')))
        file_path=os.path.join(os.path.dirname(__file__), 'test.log')
        self.log.basicConfig(filename='/home/ubuntu/jv_ws/src/doosan-robot/dsr_example/py/scripts/main/test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        self.customLog=self.log.getLogger('__name__')
        fp=self.log.FileHandler("/home/ubuntu/jv_ws/src/doosan-robot/dsr_example/py/scripts/main/test.log")
        self.customLog.setLevel(logging.DEBUG)
        self.customLog.addHandler(fp)
        self.customLog.debug('This is a debug message')
        # self.log.setLevel(logging.DEBUG)
        # self.log
        
        print(self.log)
    def writeDebug(self,msg):
        self.customLog.debug(f'Debug:{datetime.datetime.now()} - {msg}')
    def writeInfo(self,msg):
       # print("info")
    #    print(msg)
        self.customLog.info(f'Info:{datetime.datetime.now()} - {msg}')
      #  print("info ended")
    def writeError(self,msg):
         self.customLog.error(f'Error:{datetime.datetime.now()} - {msg}')
    def writeWarning(self,msg):
         self.customLog.warning(f'Warning:{datetime.datetime.now()} - {msg}')
    def writeCritical(self,msg):
         self.customLog.critical(f'Critical:{datetime.datetime.now()} - {msg}')
        #logging.warning('This is a warning message')    
        #logging.critical('This is a critical message')
    def logReload(self):
        print("reloading")
        reload(logging)

logFile=logHandling()

if __name__ == "__main__": 
  while not rospy.is_shutdown():
      pass