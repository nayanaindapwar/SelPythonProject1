# Sorting Tables

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Click on column header
# Collect all vegetable names - VeggieList
# Sort the VeggieList with the help of feature provided by browser
# Sort the VeggieList by using sorting logic
# Compare both the sorted lists

# Click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebelements = driver.find_elements(By.XPATH, "//tr//td[1]")
for ele in veggieWebelements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList












