import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumPython1Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'../drivers/geckodriver.exe')

    def tearDown(self):
        self.driver.close()

    def test_search_Pypi(self):
        driver = self.driver
        driver.get("http://python.org")
        assert "Python" in driver.title
        driver.find_element_by_class_name('pypi-meta').click()
        assert "PyPI" in driver.title
        elemSearch = driver.find_element_by_name("term")
        elemSearch.send_keys("appium")
        elemSearch.send_keys(Keys.ENTER)
        #driver.find_element_by_link_text('Login').click()

if __name__ == '__main__':
    unittest.main()