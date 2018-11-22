#coding=utf-8
from appium import Webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_driver():
    capabilities = {
        "platformName":"Android",
        "automationName":"UiAutomator2",
        "deviceName":"127.0.0.1:21503",
        "app":"",
        "appWaitActivity":"",
        "noReset":"true"
    }


























