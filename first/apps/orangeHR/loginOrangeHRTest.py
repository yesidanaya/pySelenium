import unittest
from selenium import webdriver
from loginOrangeHR import LoginOrangeHR

class LoginOrangeHRTest(unittest.TestCase):

    def setUp(self):
        self.login = LoginOrangeHR(webdriver.Firefox(executable_path=r'../../drivers/geckodriver.exe'))

    def tearDown(self):
        self.login.exit()

    def test_search_Pypi(self):
        login = self.login
        login.go_to(url='http://opensource.demo.orangehrmlive.com/')
        login.input_user(id_user_input='txtUsername', userName='Admin')
        login.input_passwd(id_passwd='txtPassword', passwd='admin')
        login.do_login(id_login='btnLogin')
        tab = login.driver.find_element_by_class_name('current')
        assert 'Dashboard' == tab.text

if __name__ == '__main__':
    unittest.main()