from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class AddEmployee:

    def __init__(self, driver):
        self.driver = driver

    def input_employee_info(self, first_name, middle_name, last_name, employee_id, check_login_details):
        driver = self.driver
        self.input_first_name(first_name)
        self.input_middle_name(middle_name)
        self.input_last_name(last_name)
        self.input_employee_id(employee_id)
        self.check_login_details_box(check_login_details)

    def input_first_name(self, first_name):
        driver = self.driver
        element = driver.find_element_by_id('firstName')
        element.send_keys(first_name)

    def input_middle_name(self, middle_name):
        driver = self.driver
        element = driver.find_element_by_id('middleName')
        element.send_keys(middle_name)

    def input_last_name(self, last_name):
        driver = self.driver
        element = driver.find_element_by_id('lastName')
        element.send_keys(last_name)

    def input_employee_id(self, employee_id):
        driver = self.driver
        element = driver.find_element_by_id('employeeId')
        element.send_keys(employee_id)

    def check_login_details_box(self, check_login_details):
        driver = self.driver
        element = driver.find_element_by_id('chkLogin')
        if check_login_details:
            element.click()

    def perform_save(self):
        driver = self.driver
        element = driver.find_element_by_id('btnSave')
        element.click()

    def validation_error_is_present(self):
        driver = self.driver
        try:
            element = driver.find_element_by_class_name('validation-error')
            return element is not None
        except NoSuchElementException:
            return False

    def add_details_info(self, user_name, password, conf_password, status):
        driver = self.driver
        self.input_user_name(user_name)
        self.input_password(password)
        self.input_confirm_password(conf_password)
        self.select_status(status)

    def input_user_name(self, user_name):
        driver = self.driver
        element = driver.find_element_by_id('user_name')
        element.send_keys(user_name)

    def input_password(self, password):
        driver = self.driver
        element = driver.find_element_by_id('user_password')
        element.send_keys(password)

    def input_confirm_password(self, confirm_password):
        driver = self.driver
        element = driver.find_element_by_id('re_password')
        element.send_keys(confirm_password)

    def select_status(self, status):
        driver = self.driver
        element = driver.find_element_by_id('status')
        select = Select(element)
        select.select_by_visible_text(status)
