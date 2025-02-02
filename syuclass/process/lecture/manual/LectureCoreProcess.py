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
import math
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.api import API
from syuclass.utils.Logger import Logger

class LectureCoreProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, OPTIONS: dict, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
    
    self.SEMESTER_NUM = {
      "1학기 정규": "0",
      "1학기 계절": "1",
      "2학기 정규": "2",
      "2학기 계절": "3",
    }
  
  def onRun(self) -> None:
    self.DRIVER.switch_to.frame("iframe1")
    self.DRIVER.switch_to.frame("ifrForm")
    
    GETYEAR = WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ipF_YY\"]"))
    )
    GETYEAR.click()
    
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.BACK_SPACE)
    GETYEAR.send_keys(Keys.BACK_SPACE)
    GETYEAR.send_keys(self.OPTIONS["year"][-2])
    GETYEAR.send_keys(self.OPTIONS["year"][-1])
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_SHTM_CD\"]"))
    ).click()
    
    semester = "//*[@id=\"sbF_SHTM_CD_itemTable_" + self.SEMESTER_NUM[self.OPTIONS["semester"]] +"\"]"
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, semester))
    ).click()
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]"))
    ).click()
    
    soup = BeautifulSoup(self.DRIVER.page_source, "html.parser")
    
    collegeTDS = soup.select("table[id=\"sbF_FCLT_CD_itemTable_main\"] tbody tr td")[1:]
    
    for collegeTD in collegeTDS:
      WebDriverWait(self.DRIVER, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"" + collegeTD["id"] + "\"]"))
      ).click()
      
      self.DRIVER.switch_to.default_content()
      self.DRIVER.switch_to.frame("iframe1")
      
      WebDriverWait(self.DRIVER, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"tgSelect\"]"))
      ).click()
      
      WebDriverWait(self.DRIVER, 10).until(
        lambda driver: driver.find_element(By.XPATH, "//*[@id=\"opStatus\"]").text != "자료를 조회 중입니다."
      )
      
      self.DRIVER.switch_to.frame("ifrForm")
      
      LECTURES_COUNT = int(self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0_column177\"]").text[:-1])
      SCROLL_COUNT = math.floor((LECTURES_COUNT - 1) / 13)
      
      around_time = -1
      
      # print(collegeTD.text + " " + str(LECTURES_COUNT) + "개")
      
      self.API = API(self.OPTIONS)
      
      while True:
        tr_count = 0
        around_time += 1
        maxStatus = False
        
        if around_time > SCROLL_COUNT:
          break
        
        soup = BeautifulSoup(self.DRIVER.page_source, "html.parser")
      
        for tr in soup.select("tbody[id=\"gdM0_F0_body_tbody\"] tr"):
          tr_count += 1
          td_index = -1
          rawLectureInfo = []
          text = ""
          
          if tr_count == 14:
            WebDriverWait(self.DRIVER, 10).until(
              lambda driver: driver.find_element(By.XPATH, "//*[@id=\"gdM0_F0\"]")
            ).send_keys(Keys.PAGE_DOWN)
            tr_count = 0
            
            if around_time < SCROLL_COUNT:
              break
          
          if maxStatus:
            break
          
          for td in tr.select("td"):
            td_index += 1
            rawLectureInfo.append(td.text)
            
            if rawLectureInfo[0] == "":
              break
            
            if around_time == SCROLL_COUNT and int(rawLectureInfo[0]) <= around_time * 13:
              break
            
            if int(rawLectureInfo[0]) == LECTURES_COUNT:
              maxStatus = True
            
            if td_index > 15:
              continue
            
            text += td.text + " "
          
          if not text:
            continue
          
          self.API.lectureManualWrite(rawLectureInfo)
          
          if self.OPTIONS["debugger"]:
            self.LOGGER.debuggerInfo(text)
        
      self.API.jsonWrite("수강편람", collegeTD.text)
      
      WebDriverWait(self.DRIVER, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]"))
      ).click()
