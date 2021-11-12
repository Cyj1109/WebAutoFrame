import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from WebAutoFrame.framework.logger import Logger

logger = Logger(logger="BasePage").getlog()

class BasePage:
    '''
    定义一个页面基类,让所有页面都继承这个类,封装一些常用的
    '''

    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        '''关闭浏览器并结束'''
        self.driver.quit()
        logger.info("quit browser and end testing.")

    def forward(self):
        '''浏览器前进操作'''
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        '''浏览器后退操作'''
        self.driver.back()
        logger.info("Click back on current page.")

    def wait(self, seconds):
        '''隐匿等待'''
        self.driver.implicity_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def close(self):
        '''关闭当前窗口'''
        self.driver.close()
        logger.info("Closing and quit the browser.")

    def get_windows_img(self):
        '''
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./screenshots/下
        :return:
        '''
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        self.driver.get_screenshot_as_file(screen_name)
        logger.info("Had take screenshot and save to folder:/screenshots")

    def find_element(self, selector):
        '''
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpth=>//*[@id='su']"
        如果采等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        '''
        element = ''
        if '=>' not in selector:
            return self.driver.find_element(By.ID, selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            element = self.driver.find_element(By.ID, selector_value)
        elif selector_by == 'n' or selector_by =='name':
            element = self.driver.find_element(By.NAME, selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element(By.CLASS_NAME, selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME, selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.driver.find_element(By.XPATH, selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            element = self.driver.find_element(By.CSS_SELECTOR, selector_value)

        return element

    def type(self, selector, text):
        '''输入'''
        el = self.find_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        '''
        点击元素
        :param selector:
        :return:
        '''
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element %s was clicked" % el.text)
        except NameError as e:
            logger.info("Failed to click the element with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("sleep for %d seconds." % seconds)