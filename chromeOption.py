# Different Chrome Options
# Refer below link to check different chrome options
# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=800,600")
chrome_options.add_argument("--disable-dev-shm-usage")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

