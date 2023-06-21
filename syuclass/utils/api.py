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
import json

from syuclass.utils.Logger import Logger

class API:
  def __init__(self, OPTIONS: dict, LOGGER: Logger):
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
    
    self.apiData = []
  
  def lectureNameWrite(self, college: str, undergraduate: str, identification: int) -> None:
    self.apiData.append({
      "단과대학": college,
      "학부(과)": undergraduate,
      "식별번호": identification,
    })
  
  def lectureInfoWrite(self, rawLectureInfo: str) -> None:
    self.apiData.append({
      "순번": rawLectureInfo[0],
      "강좌번호": rawLectureInfo[2],
      "과목코드": rawLectureInfo[3],
      "과목명": rawLectureInfo[4],
      "학부(과)": rawLectureInfo[5],
      "학년": rawLectureInfo[7],
      "이수구분": rawLectureInfo[8],
      "영역구분": rawLectureInfo[9],
      "학점": rawLectureInfo[10],
      "교수명": "" if not rawLectureInfo[13] else rawLectureInfo[13],
      "수업시간/장소": "" if not rawLectureInfo[14] else rawLectureInfo[14],
      "수업시간": "" if not rawLectureInfo[15] else rawLectureInfo[15],
      "장소": "" if not rawLectureInfo[16] else rawLectureInfo[16],
    })
  
  def jsonWrite(self, dirName: str, pathName: str) -> None:
    DATA_PATH = "../../data/"
    YS_PATH = self.OPTIONS["year"] + "/" + self.OPTIONS["semester"] + "/"
    REAL_PATH = DATA_PATH + YS_PATH
    
    if not os.path.exists(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName)):
      os.makedirs(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName))
    
    self.API_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName + "/" + pathName + ".json"))
    
    apiJson = {}
    # apiJson["time"] = self.LOGGER.getTime()
    apiJson["api"] = self.apiData
    
    with open(self.API_PATH, "w", encoding = "utf-8") as f:
      json.dump(apiJson, f, ensure_ascii = False, indent = 2)
    
    self.LOGGER.debuggerInfo("Check the file: " + self.API_PATH)