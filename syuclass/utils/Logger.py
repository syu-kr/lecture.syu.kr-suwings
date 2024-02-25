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

from syuclass.config.ConfigManager import ConfigManager

class Logger:
  def __init__(self):
    # self.CONFIG = ConfigManager()
    pass
  
  def getTime(self) -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  def logo(self) -> None:
    logo = """
   .d8888b.  888     888 888       888 8888888 888b    888  .d8888b.   .d8888b.             .d8888b.  8888888b.         d8888 888       888 888      8888888 888b    888  .d8888b.  
  d88P  Y88b 888     888 888   o   888   888   8888b   888 d88P  Y88b d88P  Y88b           d88P  Y88b 888   Y88b       d88888 888   o   888 888        888   8888b   888 d88P  Y88b 
  Y88b.      888     888 888  d8b  888   888   88888b  888 888    888 Y88b.                888    888 888    888      d88P888 888  d8b  888 888        888   88888b  888 888    888 
   "Y888b.   888     888 888 d888b 888   888   888Y88b 888 888         "Y888b.             888        888   d88P     d88P 888 888 d888b 888 888        888   888Y88b 888 888        
      "Y88b. 888     888 888d88888b888   888   888 Y88b888 888  88888     "Y88b.           888        8888888P"     d88P  888 888d88888b888 888        888   888 Y88b888 888  88888 
        "888 888     888 88888P Y88888   888   888  Y88888 888    888       "888           888    888 888 T88b     d88P   888 88888P Y88888 888        888   888  Y88888 888    888 
  Y88b  d88P Y88b. .d88P 8888P   Y8888   888   888   Y8888 Y88b  d88P Y88b  d88P           Y88b  d88P 888  T88b   d8888888888 8888P   Y8888 888        888   888   Y8888 Y88b  d88P 
   "Y8888P"   "Y88888P"  888P     Y888 8888888 888    Y888  "Y8888P88  "Y8888P"             "Y8888P"  888   T88b d88P     888 888P     Y888 88888888 8888888 888    Y888  "Y8888P88
    """
    sys.stdout.write(logo)
  
  def info(self, text: str) -> None:
    sys.stdout.write("[" + self.getTime() + "] [INFO] " + text + "\n")
  
  def debuggerInfo(self, text: str) -> None:
    sys.stdout.write("[" + self.getTime() + "] [DEBUG] " + text + "\n")
  
  def progress(self, iteration: int, total: int, decimals: int = 1, barLength: int = 100) -> None:
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