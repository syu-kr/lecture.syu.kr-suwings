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
from syuclass.config.ConfigManager import ConfigManager
from syuclass.process.ProcessManager import ProcessManager

DEBUGGER = False # Default: False

CONFIGMANAGER = ConfigManager(DEBUGGER)
CONFIG_OPTIONS = CONFIGMANAGER.onRun()

PROCESSMANAGER = ProcessManager(CONFIG_OPTIONS, DEBUGGER)
PROCESSMANAGER.onRun()