from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money_element = driver.find_element(By.ID,"money")

buy_cursor = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
buy_factory = driver.find_element(By.ID, "buyFactory")
buy_mine = driver.find_element(By.ID, "buyMine")
buy_shipment = driver.find_element(By.ID, "buyShipment")
buy_alchemy = driver.find_element(By.ID, "buyAlchemy lab")
buy_portal = driver.find_element(By.ID, "buyPortal")
buy_time_machine = driver.find_element(By.ID, "buyTime machine")
buy_elder_pledge = driver.find_element(By.ID, "buyElder Pledge")

producers = [buy_cursor, buy_grandma, buy_factory, buy_mine, buy_shipment, buy_alchemy, buy_portal, buy_time_machine, buy_elder_pledge]

def get_producer_price(producer):
    price = int(producer.find_element(By.TAG_NAME, "b").text.split("-")[-1].strip())
    return price

check_interval = 3

# while True:
time_start = time.time()
while time.time() < time_start + check_interval:
    cookie.click()
money = int(money_element.text)
print(f"Money: {money}") #TEST
for producer in reversed(producers):
    producer_type = producer.get_attribute("id")
    print(f"Producer: {producer_type}") #TEST
    if producer.get_attribute("class") == "grayed":
        continue
    price = get_producer_price(producer)
    print(f"Price: {price}") #TEST
    if money > price:
        producer.click()

driver.quit()

