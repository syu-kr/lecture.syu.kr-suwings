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
import json
import os
import sys

from syuclass.utils.Logger import Logger

class ConfigManager:
  def __init__(self, DEBUGGER):
    self.LOGGER = Logger(DEBUGGER)
  
  def onRun(self) -> dict:
    DATA_PATH = "../../"
    REAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), DATA_PATH + "/config.json"))
    
    if not os.path.exists(REAL_PATH):
      configData = {
        "dev": False,
        "userid": "test1234",
        "passwd": "test1234",
        "check_year": False,
        "check_semester": False,
        "check_college": False,
        "check_grade": False,
        "year": "2023",
        "semester": "1학기 정규",
        "grade": "전체"
      }
      
      with open(REAL_PATH, "w", encoding = "utf-8") as f:
        json.dump(configData, f, ensure_ascii = False, indent = 2)
      
      self.LOGGER.info("Check the file: " + REAL_PATH)
      self.LOGGER.info("Set the config.json data.")
      sys.exit()
      
    with open(REAL_PATH, "r", encoding = "utf-8") as f:
      JSON_DATA = json.load(f)
      
      return {
        "dev": JSON_DATA["dev"],
        "userid": JSON_DATA["userid"],
        "passwd": JSON_DATA["passwd"],
        "check_year": JSON_DATA["check_year"],
        "check_semester": JSON_DATA["check_semester"],
        "check_college": JSON_DATA["check_college"],
        "check_grade": JSON_DATA["check_grade"],
        "year": JSON_DATA["year"],
        "semester": JSON_DATA["semester"],
        "grade": JSON_DATA["grade"],
      }