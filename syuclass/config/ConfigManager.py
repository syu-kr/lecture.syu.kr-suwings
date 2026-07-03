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

# from syuclass.utils.Logger import Logger


class ConfigManager:
  DEFAULT_CONFIG = {
    "debugger": False,
    "browser_head": False,
    "userid": "test1234",
    "passwd": "test1234",
    "check_year": False,
    "check_semester": False,
    "check_college": False,
    "check_grade": False,
    "type": "d",
    "year": "2023",
    "semester": "1학기 정규",
    "grade": "전체",
  }

  ENVIRONMENT_KEYS = {
    "debugger": "SYU_DEBUGGER",
    "browser_head": "SYU_BROWSER_HEAD",
    "userid": "SYU_USERID",
    "passwd": "SYU_PASSWD",
    "check_year": "SYU_CHECK_YEAR",
    "check_semester": "SYU_CHECK_SEMESTER",
    "check_college": "SYU_CHECK_COLLEGE",
    "check_grade": "SYU_CHECK_GRADE",
    "type": "SYU_TYPE",
    "year": "SYU_YEAR",
    "semester": "SYU_SEMESTER",
    "grade": "SYU_GRADE",
  }

  VALID_TYPES = {"d", "m", "a"}
  VALID_SEMESTERS = {
    "1학기 정규",
    "1학기 계절",
    "2학기 정규",
    "2학기 계절",
  }
  VALID_GRADES = {
    "전체",
    "1학년",
    "2학년",
    "3학년",
    "4학년",
    "5학년",
    "6학년",
    "7학년",
    "8학년",
  }

  def __init__(self):
    # self.LOGGER = Logger()
    pass

  def getConfigPath(self) -> str:
    default_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config.json"))
    custom_config_path = os.getenv("SYU_CONFIG_PATH")

    if not custom_config_path:
      return default_path

    if os.path.isabs(custom_config_path):
      return custom_config_path

    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../", custom_config_path))

  def loadEnvironmentConfig(self) -> dict:
    environment_config = {}

    for config_key, env_key in self.ENVIRONMENT_KEYS.items():
      env_value = os.getenv(env_key)

      if env_value is not None and env_value != "":
        environment_config[config_key] = env_value

    return environment_config

  def parseBoolean(self, value) -> bool:
    if isinstance(value, bool):
      return value

    if isinstance(value, str):
      normalized = value.strip().lower()

      if normalized in {"1", "true", "yes", "on"}:
        return True

      if normalized in {"0", "false", "no", "off"}:
        return False

    return bool(value)

  def normalizeType(self, lecture_type) -> str:
    normalized = str(lecture_type).strip().lower()

    if normalized not in self.VALID_TYPES:
      raise ValueError("Unsupported lecture type: " + str(lecture_type))

    return normalized

  def normalizeSemester(self, semester) -> str:
    normalized = str(semester).strip()

    if normalized not in self.VALID_SEMESTERS:
      raise ValueError("Unsupported semester: " + str(semester))

    return normalized

  def normalizeGrade(self, grade) -> str:
    normalized = str(grade).strip()

    if normalized not in self.VALID_GRADES:
      raise ValueError("Unsupported grade: " + str(grade))

    return normalized

  def buildConfig(self, raw_config: dict) -> dict:
    config = dict(self.DEFAULT_CONFIG)
    config.update(raw_config)

    config["debugger"] = self.parseBoolean(config["debugger"])
    config["browser_head"] = self.parseBoolean(config["browser_head"])
    config["check_year"] = self.parseBoolean(config["check_year"])
    config["check_semester"] = self.parseBoolean(config["check_semester"])
    config["check_college"] = self.parseBoolean(config["check_college"])
    config["check_grade"] = self.parseBoolean(config["check_grade"])
    config["type"] = self.normalizeType(config["type"])
    config["year"] = str(config["year"]).strip()
    config["semester"] = self.normalizeSemester(config["semester"])
    config["grade"] = self.normalizeGrade(config["grade"])

    return config

  def onRun(self) -> dict:
    real_path = self.getConfigPath()
    environment_config = self.loadEnvironmentConfig()

    if not os.path.exists(real_path):
      if not environment_config:
        with open(real_path, "w", encoding = "utf-8") as f:
          json.dump(self.DEFAULT_CONFIG, f, ensure_ascii = False, indent = 2)

        # self.LOGGER.info("Check the file: " + real_path)
        # self.LOGGER.info("Set the config.json data.")
        sys.exit()

      return self.buildConfig(environment_config)

    with open(real_path, "r", encoding = "utf-8") as f:
      json_data = json.load(f)

    json_data.update(environment_config)

    return self.buildConfig(json_data)
