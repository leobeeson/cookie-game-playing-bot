from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
money = driver.find_element_by_id("money")

buy_cursor = driver.find_element_by_id("buyCursor")
buy_grandma = driver.find_element_by_id("buyGrandma")
buy_factory = driver.find_element_by_id("buyFactory")
buy_mine = driver.find_element_by_id("buyMine")
buy_shipment = driver.find_element_by_id("buyShipment")
buy_alchemy = driver.find_element_by_id("buyAlchemy")
buy_portal = driver.find_element_by_id("buyPortal")
buy_time_machine = driver.find_element_by_id("buyTime machine")
buy_elder_pledge = driver.find_element_by_id("buyElder Pledge")

check_interval = 5

time_start = time.time()

while time.time() < time_start + check_interval:
    cookie.click()


driver.quit()