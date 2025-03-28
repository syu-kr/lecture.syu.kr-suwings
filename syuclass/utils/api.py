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
  def __init__(self, OPTIONS: dict):
    self.OPTIONS = OPTIONS
    self.LOGGER = Logger()
    
    self.apiData = []
  
  def lectureNameWrite(self, college: str, undergraduate: str, identification: int) -> None:
    self.apiData.append({
      "단과대학": college,
      "학부(과)": undergraduate,
      "식별번호": identification,
    })
  
  def lectureDescriptionWrite(self, rawLectureInfo: str) -> None:
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
  
  def lectureManualWrite(self, rawLectureInfo: str) -> None:
    self.apiData.append({
      "순번": rawLectureInfo[0],
      "강좌번호": rawLectureInfo[6],
      "과목코드": rawLectureInfo[5],
      "과목명": rawLectureInfo[7],
      "학부(과)": rawLectureInfo[2],
      "학년": rawLectureInfo[3][:-2],
      "이수구분": rawLectureInfo[4],
      "영역구분": rawLectureInfo[10],
      "학점": rawLectureInfo[8],
      "교수명": "" if not rawLectureInfo[11] else rawLectureInfo[11],
      "수업시간": "" if not rawLectureInfo[12] else rawLectureInfo[12],
      "장소": "" if not rawLectureInfo[13] else rawLectureInfo[13],
      "비고": "" if not rawLectureInfo[14] else rawLectureInfo[14],
      "팀티칭여부": "" if not rawLectureInfo[15] else rawLectureInfo[15],
    })
  
  def jsonWrite(self, dirName: str, pathName: str) -> None:
    DATA_PATH = "../../data/"
    YS_PATH = self.OPTIONS["year"] + "/" + self.OPTIONS["semester"] + "/"
    REAL_PATH = DATA_PATH + YS_PATH
    
    if not os.path.exists(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName)):
      os.makedirs(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName))
    
    self.API_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), REAL_PATH + dirName + "/" + pathName + ".json"))
    
    apiJson = {}
    apiJson["api"] = []
    
    # apiJson["time"] = self.LOGGER.getTime()
    # apiJson["api"] = self.apiData

    deduplication = {}

    for i in self.apiData:
      if "순번" in i:
        deduplication[i["순번"]] = i
      else:
        apiJson["api"].append(i)
    
    apiJson["api"] += list(deduplication.values())
    
    with open(self.API_PATH, "w", encoding = "utf-8") as f:
      json.dump(apiJson, f, ensure_ascii = False, indent = 2)
    
    if self.OPTIONS["debugger"]:
      self.LOGGER.debuggerInfo("Check the file: " + self.API_PATH)
