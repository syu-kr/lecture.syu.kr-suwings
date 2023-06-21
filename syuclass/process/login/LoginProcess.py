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

class LoginProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, OPTIONS: dict, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
  
  def onRun(self) -> None:
    WebDriverWait(self.DRIVER, 10).until(
      lambda driver: driver.execute_script("return webcrypto").get("e2e") != None
    )
    
    userid = WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"edId\"]"))
    )
    password = WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"edPass\"]"))
    )
    login_button = WebDriverWait(self.DRIVER, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id=\"imgLogin\"]"))
    )

    userid.click()
    userid.send_keys(self.OPTIONS["userid"])

    password.click()
    password.send_keys(self.OPTIONS["passwd"])
    
    login_button.click()
    
    self.LOGGER.info("LoginProcess succeeded...")
    
    # try:
    #   WebDriverWait(self.DRIVER, 10).until(EC.alert_is_present())
      
    #   self.LOGGER.info(self.DRIVER.switch_to.alert.text)
    #   self.LOGGER.info("LoginProcess failed...")
      
    #   self.DRIVER.quit()
    #   sys.exit()
    # except:
    #   self.LOGGER.info("LoginProcess succeeded...")