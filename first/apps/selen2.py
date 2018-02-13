import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumPython2Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'../drivers/chromedriver.exe')

    def tearDown(self):
        self.driver.close()

    def test_search_Pypi(self):
        self.driver.get("http://python.org")
        assert "Python" in self.driver.title
        self.driver.find_element_by_class_name('pypi-meta').click()
        assert "PyPI" in self.driver.title
        elemSearch = self.driver.find_element_by_name("term")
        elemSearch.send_keys("appium")
        elemSearch.send_keys(Keys.ENTER)
        #driver.find_element_by_link_text('Login').click()

if __name__ == '__main__':
    unittest.main()