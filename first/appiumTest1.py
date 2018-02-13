# Android environment
import unittest

import selenium
from appium import webdriver
from pathlib import Path

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = Path('/apps/selendroid-test-app.apk')

webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


