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
import sys

class Logger:
  def __init__(self, DEBUGGER: bool = False):
    self.DEBUGGER = DEBUGGER
  
  def getTime(self) -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  def logo(self) -> None:
    logo = f"""
                                           __                                         _           __ 
              _______  ____  __      _____/ /___ ___________      ____  _________    (_)__  _____/ /_
             / ___/ / / / / / /_____/ ___/ / __ `/ ___/ ___/_____/ __ \/ ___/ __ \  / / _ \/ ___/ __/
            (__  ) /_/ / /_/ /_____/ /__/ / /_/ (__  |__  )_____/ /_/ / /  / /_/ / / /  __/ /__/ /_  
           /____/\__, /\__,_/      \___/_/\__,_/____/____/     / .___/_/   \____/_/ /\___/\___/\__/  
                /____/                                        /_/              /___/                 
          
          Unofficial su-wings (SAHMYOOK UNIV.) lecture information system.
          Github: https://github.com/0verfl0w767/syu-class-api
          Author: 0verfl0w767 (https://github.com/0verfl0w767)
          Version: 1.0v
          License: MIT LICENSE
          Debugger: {self.DEBUGGER}
          
    """
    sys.stdout.write(logo)
  
  def info(self, text: str) -> None:
    sys.stdout.write("[" + self.getTime() + "] [INFO] " + text + "\n")
  
  def debuggerInfo(self, text: str) -> None:
    if self.DEBUGGER == True:
      sys.stdout.write("[" + self.getTime() + "] [DEBUGGER] " + text + "\n")
  
  def progress(self, iteration: int, total: int, decimals: int = 1, barLength: int = 100) -> None:
    if self.DEBUGGER == False:
      formatStr = "{0:." + str(decimals) + "f}"
      
      if iteration == 0 and total == 0:
        percent = formatStr.format(total)
        bar = "\033[101m-\033[0m" * barLength
        
        sys.stdout.write("\r%s [%s] %s%s " % ("[" + self.getTime() + "] [INFO]", bar, percent, "%"))
        sys.stdout.write("(abolished)")
        sys.stdout.write("\n")
        sys.stdout.flush()
        return
      
      percent = formatStr.format(100 * (iteration / float(total)))
      filledLength = int(round(barLength * iteration / float(total)))
      bar = "\033[102m#\033[0m" * filledLength + "\033[100m-\033[0m" * (barLength - filledLength)
      
      sys.stdout.write("\r%s [%s] %s%s " % ("[" + self.getTime() + "] [INFO]", bar, percent, "%"))
      
      if iteration == total:
        sys.stdout.write("(completed)")
        sys.stdout.write("\n")
        sys.stdout.flush()