import os
import configparser
from .logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine:

    dir = os.path.dirname(os.path.abspath('.'))   #注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver


    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path, encoding='UTF-8') 如果代码中有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")
        logger.info("The test server url is:%s" % url)