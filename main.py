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
import os
import subprocess
import sys

def install_requirements(requirements_file):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            text=True,
            capture_output=True,
            check=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e)
    except Exception as e:
        print(e)

def is_truthy(value):
    if value is None:
        return False

    return str(value).strip().lower() in {"1", "true", "yes", "on"}

if not is_truthy(os.getenv("SYU_SKIP_REQUIREMENTS_INSTALL")):
    install_requirements("requirements.txt")

from syuclass.config.ConfigManager import ConfigManager
from syuclass.process.ProcessManager import ProcessManager

CONFIGMANAGER = ConfigManager()
CONFIG_OPTIONS = CONFIGMANAGER.onRun()

PROCESSMANAGER = ProcessManager(CONFIG_OPTIONS)
PROCESSMANAGER.onRun()
