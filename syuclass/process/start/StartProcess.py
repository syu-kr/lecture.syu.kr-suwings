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
# from webdriver_manager.chrome import ChromeDriverManager
# import os
# import chromedriver_autoinstaller

import os

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.Logger import Logger


class StartProcess(BaseProcess):
  def __init__(self, OPTIONS: dict, LOGGER: Logger):
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER

  def onRun(self) -> None:
    # Not work: os.path.exists("C:\\Users\\kim\\Desktop\\Chromium.exe")

    # DRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../driver/"))
    # CHROMIUM_VER = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
    # CHROMIUM_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../driver/" + CHROMIUM_VER + "/chromedriver.exe"))

    # if not os.path.exists(DRIVER_PATH):
    #   os.makedirs(DRIVER_PATH)

    #   self.LOGGER.info("Chromedriver is not found...")
    #   self.LOGGER.info("Start a manual download...")

    #   chromedriver_autoinstaller.install(False, DRIVER_PATH)

    #   self.LOGGER.info("Check the driver: " + CHROMIUM_PATH)

    options = Options()

    if not self.OPTIONS["browser_head"]:
      options.add_argument("--headless")

    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
      options.add_argument("--no-sandbox")
      options.add_argument("--disable-dev-shm-usage")

    chrome_binary = os.getenv("CHROME_BIN")
    chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")

    if chrome_binary:
      options.binary_location = chrome_binary

    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")

    # self.DRIVER = webdriver.Chrome(service=Service(CHROMIUM_PATH), options = options)
    # self.DRIVER = webdriver.Chrome(ChromeDriverManager().install())
    if chrome_driver_path:
      self.DRIVER = webdriver.Chrome(service = Service(chrome_driver_path), options = options)
    else:
      self.DRIVER = webdriver.Chrome(options = options)

    self.DRIVER.get("https://suwings.syu.ac.kr/sso/login.jsp")

    self.LOGGER.info(self.OPTIONS["year"] + " - " + self.OPTIONS["semester"])
    self.LOGGER.info("StartProcess succeeded...")
