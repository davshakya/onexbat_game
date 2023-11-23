from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class LocatorX:
    airplane_loc = "//*[@fill='#de8a06']"
    block_popup_loc = "//a[contains(text(),'Block')]"
