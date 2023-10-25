# ----WAIT DEMO -----

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) # Here we can't remove the wait as below statement is find_elements, it will create the list of elements, initially empty list is genereated so it might confusing, after waiting foe 2 mins, it will load all the elements of the list.

results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(results)

assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum =0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

# driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)




