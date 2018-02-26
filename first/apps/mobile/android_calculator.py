import unittest
from time import sleep

from appium import webdriver


# Returns abs path relative to this file and not cwd


class ComplexAndroidTests(unittest.TestCase):
    """
    Android Calculator Test.
    """
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_calculator_operation(self):
        # pause a moment, so xml generation can occur
        sleep(2)
        self.driver.find_element_by_id('com.android.calculator2:id/digit9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/plus').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/equal').click()

        # verify the result
        editor_result = self.driver.find_element_by_class_name('android.widget.EditText')
        assert '14' == editor_result.text


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
