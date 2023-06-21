#
#     ____                  __________
#    / __ \_   _____  _____/ __/ / __ \_      __
#   / / / / | / / _ \/ ___/ /_/ / / / / | /| / /
#  / /_/ /| |/ /  __/ /  / __/ / /_/ /| |/ |/ /
#  \____/ |___/\___/_/  /_/ /_/\____/ |__/|__/
# 
#  The copyright indication and this authorization indication shall be
#  recorded in all copies or in important parts of the Software.
# 
#  @author 0verfl0w767
#  @link https://github.com/0verfl0w767
#  @license MIT LICENSE
#
import datetime
import os
import signal
import time

from syuclass.process.start.StartProcess import StartProcess
from syuclass.process.login.LoginProcess import LoginProcess
from syuclass.process.lecture.LectureInfoProcess import LectureInfoProcess
from syuclass.process.lecture.LectureScanProcess import LectureScanProcess
from syuclass.utils.Logger import Logger

class ProcessManager:
  def __init__(self, OPTIONS: dict, DEBUGGER: bool):
    self.OPTIONS = OPTIONS
    
    self.LOGGER = Logger(DEBUGGER)
      
  def onRun(self) -> None:
    self.LOGGER.logo()
    
    start = time.time()
    
    SP = StartProcess(self.OPTIONS, self.LOGGER)
    SP.onRun()
      
    try:
      LP = LoginProcess(SP.DRIVER, self.OPTIONS, self.LOGGER)
      LP.onRun()
      
      LIP = LectureInfoProcess(SP.DRIVER, self.LOGGER)
      LIP.onRun()
      
      LSP = LectureScanProcess(SP.DRIVER, self.OPTIONS, self.LOGGER)
      LSP.onRun()
    except Exception as e:
      self.LOGGER.info("An error occurred during processing...")
      self.LOGGER.info(str(e))
    
    end = time.time()
    
    self.LOGGER.info(str(datetime.timedelta(seconds=(end - start))))
    
    # issue in pypy3.
    #
    # Traceback (most recent call last):
    #   File "C:\pypy\Lib\threading.py", line 980, in _bootstrap_inner
    #     self.run()
    #   File "C:\pypy\Lib\threading.py", line 917, in run
    #     self._target(*self._args, **self._kwargs)
    #   File "c:\Users\kim\.vscode\extensions\ms-python.python-2023.6.1\pythonFiles\lib\python\debugpy\launcher/../..\debugpy\common\messaging.py", line 1427, in _run_handlers
    #     self._parser_thread.join()
    #   File "C:\pypy\Lib\threading.py", line 1060, in join
    #     self._wait_for_tstate_lock()
    #   File "C:\pypy\Lib\threading.py", line 1081, in _wait_for_tstate_lock
    #     lock.release()
    # RuntimeError: cannot release un-acquired lock
    #
    # solved this problem. in pypy\Lib\threading.py (1066 lines)
    # "raise" code annotation inside the _wait_for_tstate_lock()
    
    SP.DRIVER.quit()