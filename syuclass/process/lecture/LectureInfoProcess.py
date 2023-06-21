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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.Logger import Logger

class LectureInfoProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
  
  def onRun(self) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"treeview1_node_24\"]"))
    ).click()
    
    WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"treeview1_node_25\"]/tbody/tr/td[3]"))
    ).click()
    
    self.LOGGER.info("LectureInfoProcess succeeded...")