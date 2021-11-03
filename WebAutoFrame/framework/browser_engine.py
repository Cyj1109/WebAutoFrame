import os
import configparser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.service import Service

from .logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine:

    dir = os.path.dirname(os.path.abspath('.'))   #注意相对路径获取方法
    chrome_service = Service(dir + '/tools/chromedriver.exe')
    ie_service = Service(dir + '/tools/iedriver.exe')

    def __init__(self, driver):
        self.driver = driver


    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path, encoding='UTF-8') 如果代码中有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is:%s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Chrome":
            driver = webdriver.Chrome(service=self.chrome_service)
        elif browser == "IE":
            driver = webdriver.Ie(service=self.ie_service)

        driver.get(url)
        logger.info("open url:%s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()