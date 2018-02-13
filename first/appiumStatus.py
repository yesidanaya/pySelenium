import selenium
from appium import webdriver

result = selenium.webdriver.common.utils.is_url_connectable('4723')

print(result)