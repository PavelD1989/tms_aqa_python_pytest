import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pytest import fixture, mark
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get("https://www.bbc.com/news")
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()
