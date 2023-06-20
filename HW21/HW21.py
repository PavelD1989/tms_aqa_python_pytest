from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pytest import fixture, mark
import time
import pytest
from conftest import helper


# 1. Проверка регистрации при заполнении всех обязательных полей_Ожидаемый результат: после регистрации
# появляется уведомление, часть которого выглядит так "Note: Your user name is  "

def test_authorization(helper):

    user_name_xpath = "//input[@name='email']"
    user_name_locator = helper.find_element(By.XPATH, user_name_xpath)
    user_name_locator.click()
    user_name_locator.send_keys('pavel')

    password_xpath = "//input[@type='password']"
    password_locator = helper.find_element(By.XPATH, password_xpath)
    password_locator.click()
    password_locator.send_keys('pass123')

    confirm_xpath = "//input[@name='confirmPassword']"
    confirm_locator = helper.find_element(By.XPATH, confirm_xpath)
    confirm_locator.click()
    confirm_locator.send_keys('pass123')


    btn_authorization_xpath = "//input[@name='submit']"
    btn_authorization_locator = helper.find_element(By.XPATH, btn_authorization_xpath)
    btn_authorization_locator.click()

    message_success_authorization_xpath = "//b[contains(text(), 'Note: Your user name is')]"
    message_success_authorization_locator = helper.find_element(By.XPATH,
                                                                message_success_authorization_xpath)
    assert message_success_authorization_locator.is_displayed()


# 2. На стрице https://demo.guru99.com/test/newtours/reservation.php радиобаттон "bussiness class" успешно устанавливается

def test_check_box_select():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://demo.guru99.com/test/newtours/reservation.php')
    driver.maximize_window()

    radio_btn_business_xpath = "//input[@value='Business']"
    radio_btn_business_locator = driver.find_element(By.XPATH, radio_btn_business_xpath)
    radio_btn_business_locator.click()
    assert radio_btn_business_locator.

    driver.close()
    driver.quit()



 # 3. Наличие элементов на странице "sign-on" "register" "support" "contact"


def test_elements_present(helper):
    sign_on_element_xpath = "//a[@href='login.php']"
    register_element_xpath = "//a[@href='register.php']"
    support_element_xpath = "//a[@href='support.php']"
    contact_element_xpath = "//a[text()='CONTACT']"

    sign_on_element_locator = helper.find_element(By.XPATH, sign_on_element_xpath)
    register_element_locator = helper.find_element(By.XPATH, register_element_xpath)
    support_element_locator = helper.find_element(By.XPATH, support_element_xpath)
    contact_element_locator = helper.find_element(By.XPATH, contact_element_xpath)

    arr_of_elements_page = [sign_on_element_locator, register_element_locator, support_element_locator,
                            contact_element_locator]
    for i in arr_of_elements_page:
        assert i.is_displayed()


# 4. Если нажать на 'telecom project' вы перейдете на страницу 'https://demo.guru99.com/telecom/index.html'


def test_telecom_project_page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://demo.guru99.com/test/newtours/index.php')
    driver.maximize_window()

    telecom_project_xpath = "//a[text()='Telecom Project']"
    telecom_project_locator = driver.find_element(By.XPATH, telecom_project_xpath)
    telecom_project_locator.click()

    current_url = driver.current_url
    assert current_url == 'https://demo.guru99.com/telecom/index.html'

    driver.close()
    driver.quit()


# 5. Элемент "Selenium" на странице активный и кликабельный

def test_work_of_element_selenium():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://demo.guru99.com/test/newtours/index.php')
    driver.maximize_window()

    selenium_element_xpath = "//a[text()='Selenium']"
    selenium_element_locator = driver.find_element(By.XPATH, selenium_element_xpath)
    assert selenium_element_locator.is_displayed()

    driver.close()
    driver.quit()
