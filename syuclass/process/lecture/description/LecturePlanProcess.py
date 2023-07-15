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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.Logger import Logger

class LecturePlanProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, OPTIONS: dict, LOGGER: Logger, COLLEGE: str, UNDERGRADUATE: str):
    self.DRIVER = DRIVER
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
    self.COLLEGE = COLLEGE
    self.UNDERGRADUATE = UNDERGRADUATE
    
    self.SEMESTER_NUM = {
      "1학기 정규": "0",
      "1학기 계절": "1",
      "2학기 정규": "2",
      "2학기 계절": "3",
    }
    self.GRADE_NUM = {
      "전체": "0",
      "1학년": "1",
      "2학년": "2",
      "3학년": "3",
      "4학년": "4",
      "5학년": "5",
      "6학년": "6",
      "7학년": "7",
      "8학년": "8",
    }
  
  def setYear(self, year) -> None:
    GETYEAR = WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ipF_ENTR_YY\"]"))
    )
    GETYEAR.click()
    
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.BACK_SPACE)
    GETYEAR.send_keys(Keys.BACK_SPACE)
    GETYEAR.send_keys(year[-2])
    GETYEAR.send_keys(year[-1])
  
  def setSemester(self, semester) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_SHTM\"]"))
    ).click()
    
    semester = "//*[@id=\"sbF_SHTM_itemTable_" + self.SEMESTER_NUM[semester] +"\"]"
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, semester))
    ).click()
  
  def setCollege(self, college) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_COLG_CD\"]"))
    ).click()
    
    college = "//*[@id=\"" + college + "\"]"
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, college))
    ).click()
  
  def setUndergraduate(self, undergraduate) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]"))
    ).click()
    
    undergraduate = "//*[@id=\"" + undergraduate + "\"]"
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, undergraduate))
    ).click()
  
  def setGrade(self, grade) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sbF_GRDE\"]"))
    ).click()
    
    grade = "//*[@id=\"sbF_GRDE_itemTable_" + self.GRADE_NUM[grade] + "\"]"
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, grade))
    ).click()
  
  def onRun(self) -> None:
    if not self.OPTIONS["check_year"]:
      self.setYear(self.OPTIONS["year"])
      self.OPTIONS["check_year"] = True
    
    if not self.OPTIONS["check_semester"]:
      self.setSemester(self.OPTIONS["semester"])
      self.OPTIONS["check_semester"] = True
    
    if not self.OPTIONS["check_college"]:
      self.setCollege(self.COLLEGE)
      self.OPTIONS["check_college"] = True
    
    self.setUndergraduate(self.UNDERGRADUATE)
    
    if not self.OPTIONS["check_grade"]:
      self.setGrade(self.OPTIONS["grade"])
      self.OPTIONS["check_grade"] = True
    
    self.DRIVER.switch_to.default_content()
    self.DRIVER.switch_to.frame("iframe1")
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"tgSelect\"]"))
    ).click()
    