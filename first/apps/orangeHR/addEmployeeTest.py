import unittest
from selenium import webdriver
from loginOrangeHR import LoginOrangeHR
from addEmployee import AddEmployee
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginOrangeHRTest(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox(executable_path=r'../../drivers/geckodriver.exe')
        self.login = LoginOrangeHR(driver)
        self.add_employee = AddEmployee(driver)

    def tearDown(self):
        self.login.exit()

    def complete_initial(self, check_details, add_details):
        login = self.login
        add_employee = self.add_employee
        driver = login.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        login.do_successful_login()
        pim_tab = driver.find_element_by_id('menu_pim_viewPimModule')
        actions.move_to_element(pim_tab).perform()
        wait.until(EC.visibility_of_element_located((By.ID, "menu_pim_addEmployee"))).click()
        add_employee.input_employee_info('Oscar', 'Yesid', 'Anaya', '3654', check_details)
        if add_details:
            add_employee.add_details_info('oanayao', 'oanayao123', 'oanayao123', 'Enabled')

    def test_add_employee_without_login_details(self):
        login = self.login
        add_employee = self.add_employee
        self.complete_initial(check_details=True, add_details=False)
        add_employee.perform_save()
        assert add_employee.validation_error_is_present()

    def test_add_employee_with_login_details(self):
        login = self.login
        add_employee = self.add_employee
        self.complete_initial(check_details=False, add_details=False)
        add_employee.perform_save()
        assert not add_employee.validation_error_is_present()

    def test_add_employee_with_login_details_complete(self):
        login = self.login
        add_employee = self.add_employee
        self.complete_initial(check_details=True, add_details=True)
        add_employee.perform_save()
        assert not add_employee.validation_error_is_present()


if __name__ == '__main__':
    unittest.main()