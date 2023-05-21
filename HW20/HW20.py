import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pytest import fixture, mark


#Поиск элемента на странице и клик
def test_21vek_open():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.21vek.by/special_offers/dacha_all.html')
    driver.fullscreen_window()

    logo_xpath = '//*[@id="header"]/div/div[3]/div[1]'
    logo_locator = driver.find_element(By.XPATH, logo_xpath)

    time.sleep(5)
    logo_locator.click()




#Поиск на странице локатора, клик, assert адресной строки
def test_delivery():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.21vek.by/")
    driver.fullscreen_window()


    footer_xpath = '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a'
    footer_locator = driver.find_element(By.XPATH, footer_xpath)


    driver.execute_script("arguments[0].scrollIntoView();", footer_locator)

    time.sleep(3)
    footer_locator.click()


    current_url = driver.current_url
    assert current_url == 'https://www.21vek.by/services/delivery.html'