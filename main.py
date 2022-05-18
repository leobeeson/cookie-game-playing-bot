from typing import List
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def get_available_producers(driver: WebDriver) -> List[tuple]:
    producers = driver.find_elements(By.CSS_SELECTOR, "#store div")
    available_producers = [(producer, int(producer.find_element(By.TAG_NAME, "b").text.split("-")[-1].strip())) for producer in producers if producer.get_attribute("class") == ""]
    return available_producers


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
    
    available_producers = get_available_producers(driver)

    while money_amount > available_producers[-1][1]:        
        available_producers[-1][0].click()
        
        money = get_element_by_id(driver, "money")
        money_amount = int(money.text)
        available_producers = get_available_producers(driver)

driver.quit()

#TODO: Handle `StaleElementReferenceException`
#