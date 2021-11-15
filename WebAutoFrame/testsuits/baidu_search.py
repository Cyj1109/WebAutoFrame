import time
import unittest

from WebAutoFrame.framework.browser_engine import BrowserEngine
from WebAutoFrame.pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        '''
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        '''
        测试结束后的操作，这里基本都是关闭浏览器
        :return:
        '''
        cls.driver.quit()

    def test_baidu_search(self):
        '''
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        '''
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('Test pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(1)
        homepage.get_windows_img()

if __name__ == '__main__':
    unittest.main()