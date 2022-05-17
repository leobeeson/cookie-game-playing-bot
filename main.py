from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def get_available_producers(driver: WebDriver):
    producers = driver.find_elements(By.CSS_SELECTOR, "#store div")
    available_producers = [producer for producer in producers if producer.get_attribute("class") == ""]
    return available_producers


def get_producer_price(producer):
    price = int(producer.find_element(By.TAG_NAME, "b").text.split("-")[-1].strip())
    return price


def get_available_prices(driver: WebDriver):
    producers = driver.find_elements(By.CSS_SELECTOR, "#store div")
    available_prices = [get_producer_price(producer) for producer in producers if producer.get_attribute("class") == ""]
    return available_prices


def get_element_by_id(driver: WebDriver, id: str):
    element = driver.find_element(By.ID, id)
    return element


game_duration = 30
check_interval = 3

game_time_start = time.time()
while time.time() < game_time_start + game_duration:
    
    cookie = get_element_by_id(driver, "cookie")
    interval_time_start = time.time()
    while time.time() < interval_time_start + check_interval:
        cookie.click()

    money = get_element_by_id(driver, "money")
    money_amount = int(money.text)
    
    prices = get_available_prices(driver)

    while money_amount > prices[-1]:
        producers = get_available_producers(driver)
        most_expensive_producer = producers.pop()
        most_expensive_producer.click()

        
        money = get_element_by_id(driver, "money")
        money_amount = int(money.text)
        prices = get_available_prices(driver)

driver.quit()

#TODO: Handle `StaleElementReferenceException`
#