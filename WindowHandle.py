# Handling different windows in Selenium

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
time.sleep(2)
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
time.sleep(2)
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text







