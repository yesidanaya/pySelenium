from selenium import webdriver

class LoginOrangeHR:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def input_user(self, id_user_input, userName):
        userElement = self.driver.find_element_by_id(id_user_input)
        userElement.send_keys(userName)

    def input_passwd(self, id_passwd, passwd):
        passwdElement = self.driver.find_element_by_id(id_passwd)
        passwdElement.send_keys(passwd)

    def do_login(self, id_login):
        loginElement = self.driver.find_element_by_id(id_login)
        loginElement.click()

    def exit(self):
        self.driver.quit()

