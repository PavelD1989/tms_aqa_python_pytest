import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pytest import fixture, mark
from selenium.webdriver.support.ui import Select
from conftest import browser
import pytest

# -----------------ЗАДАНИЕ 1------------------------------



# #Поиск "самолета" (иной актуальной картинки)


def test_find_main_picture(browser):

    main_picture_css = 'div.gs-c-promo-image.gs-u-mb'
    main_picture_locator = browser.find_element(By.CSS_SELECTOR, main_picture_css)
    assert main_picture_locator.is_displayed()

# #Поиск логотипа "BBC"
def test_search_bbc_logo(browser):

    logo_picture_css = '#homepage-link > svg'
    logo_picture_locator = browser.find_element(By.CSS_SELECTOR, logo_picture_css)
    assert logo_picture_locator.is_displayed()

# #Поиск категории "Спорт"

def test_category_sport_clickable(browser):

    category_sport_css = '#homepage-link > svg'
    category_sport_locator = browser.find_element(By.CSS_SELECTOR, "#homepage-link > svg")

    assert category_sport_locator.is_displayed()

#Поиск нескольких категорий одновременно и проверка клика// Не разобрался как "одновременно" проверить наличие. Пробовал через цикл
#выдает ошибку StaleElementReferenceException
def test_few_category(browser):

    category_home_xpath = "//span[@aria-hidden='true'][text()='Home'][1]"
    category_climate_xpath = "//a[@class='nw-o-link']//span[text()='Climate']"

    category_home_locator = browser.find_element(By.XPATH, category_home_xpath)
    category_climate_locator = browser.find_element(By.XPATH, category_climate_xpath)

    arr_of_category = [category_home_locator, category_climate_locator]
    for i in arr_of_category:
        i.click()
        time.sleep(3)



#
# # ---------------------------------------Задание 2-----------------------------------------------

# # # - check/uncheck checkbox
#
def test_checkboxes():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('http://the-internet.herokuapp.com/checkboxes')
    driver.maximize_window()

    checkbox_first_xpath = '//*[@id="checkboxes"]/input[1]'
    checkbox_second_xpath = '//input[@type="checkbox"][@checked]'

    checkbox_first_locator = driver.find_element(By.XPATH, checkbox_first_xpath)
    checkbox_second_locator = driver.find_element(By.XPATH, checkbox_second_xpath)

    assert checkbox_second_locator.is_selected()
    assert not checkbox_first_locator.is_selected()



# # - scroll // Так понимаю проскроллил единожды вниз и упёрся.. Не уверен что верно//

def test_vertical_scroll():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/infinite_scroll")
    driver.maximize_window()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)




# # - check radio button

def test_check_radio_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")
    driver.fullscreen_window()
    driver.implicitly_wait(10)

    radio_button_impressive_to_click_xpath = "//div[2]/div[2]/div[2]/div[3]"
    radio_button_impressive_to_click_locator = driver.find_element(By.XPATH, radio_button_impressive_to_click_xpath)
    radio_button_impressive_to_click_locator.click()
    time.sleep(5)

    radio_button_impressive_checked_xpath = '//p[@class ="mt-3"]//span[@class="text-success"][text()="Impressive"]'
    radio_button_impressive_checked_locator = driver.find_element(By.XPATH, radio_button_impressive_checked_xpath)
    radio_button_impressive_checked_locator.click()

    assert radio_button_impressive_checked_locator


#
# # select value from dropdown

def test_check_dropdown():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/dropdown")
    driver.fullscreen_window()
    driver.implicitly_wait(15)

    drop_to_click_xpath = '//*[@id="dropdown"]'
    drop_to_click_locator = driver.find_element(By.XPATH, drop_to_click_xpath)
    time.sleep(5)
    select_drop = Select(drop_to_click_locator)
    time.sleep(5)
    select_drop.select_by_visible_text('Option 2')
    time.sleep(5)
    drop_option_2_is_selected_locator = driver.find_element(By.XPATH, '//option[@selected="selected"][text()="Option 2"]')
    assert drop_option_2_is_selected_locator

#
# # - ввести текст в инпут и получить введеный текст(getAttribute) НЕ РЕШИЛ



def test_input_for_find():
    driver = webdriver.Chrome()
    driver.get("https://www.21vek.by/")
    driver.fullscreen_window()
    driver.implicitly_wait(15)
    time.sleep(4)

    input_xpath = '//*[@id="catalogSearch"]'
    input_locator = driver.find_element(By.XPATH, input_xpath)
    input_locator.send_keys()
    time.sleep(4)
    input_locator.get_attribute()
    time.sleep(4)
    input_xpath.is

    abc = driver


# # getAttribute(получить значение аттрибутов class, value) НЕ РЕШИЛ
#
#
#
# # --------------------------ЗАДАНИЕ 3-------------------------------------
#
# # Привести разницу между методом isPresent(isExisted) и isDisplayed
#
#
#
#
# # - реализовать кастомное ожидание на метод isEnabled
# # - реализовать кастомное ожидание на метод isDisplayed
# #
#
#
