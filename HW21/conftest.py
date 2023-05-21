from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pytest import fixture, mark
import time
import pytest




@pytest.fixture()
def helper():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()
