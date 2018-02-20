import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Nexus 10'
        desired_caps['appPackage'] = 'io.selendroid.testapp'
        desired_caps['appActivity'] = 'io.selendroid.testapp.HomeScreenActivity'        
        desired_caps['app'] = PATH('../../apks/selendroid-test-app-0.12.0.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_elements(self):
        # pause a moment, so xml generation can occur
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId(\"io.selendroid.testapp:id/my_text_field\")').send_keys("Test Appium")                             
               

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
