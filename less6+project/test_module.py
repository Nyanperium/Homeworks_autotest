from selenium.webdriver.common.by import By
import time
from Locators.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains

def test_one(driver, adress_param):
    '''Переходим на страницу OpenCart и проверяем, что мы находимся на ней.'''
    driver.get(adress_param)
    button_currency = driver.find_element(By.CSS_SELECTOR, MainPage.Currency.currency_button)
    button_pound_sterling = driver.find_element(By.CSS_SELECTOR, MainPage.Currency.pound_sterling)
    ActionChains(driver).click(button_currency).pause(2).click(button_pound_sterling).pause(2).perform()
    driver.find_element(By.CSS_SELECTOR, MainPage.NavTop.shopping_cart).click()