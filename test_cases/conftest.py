from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest
from project_resource.locator_onex import LocatorX
from project_resource.variable_onex import VariableX


@pytest.fixture
def get_sum():
    a, b = 3, 5
    c = a + b
    return c


@pytest.fixture
def setup(request, get_sum):
    print("It will run first")
    print("Sum>>>>>>>>>>>", get_sum)
    request.cls.driver = webdriver.Chrome(service=Service(executable_path=VariableX.chrome_path))
    request.cls.driver.get(VariableX.oneX_url)
    request.cls.driver.maximize_window()
    yield
    print("It will run at the end")
    request.cls.driver.quit()
