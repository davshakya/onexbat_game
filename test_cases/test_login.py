from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest
from project_resource.locator_onex import LocatorX
from project_resource.BasePage import BasePageX


@pytest.mark.usefixtures("setup")
class Test1bat:
    def test_login_onex(self):
        WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.XPATH, LocatorX.block_popup_loc)))
        self.driver.find_element(By.XPATH, LocatorX.block_popup_loc).click()
        # self.driver.find_element(By.XPATH, LocatorX.airplane_loc).click()
        # WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.XPATH, LocatorX.airplane_loc)))
