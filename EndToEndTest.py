# End to end test

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.CSS_SELECTOR, "div[class = 'card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    print(productName)
    if productName == "Blackberry":
        # Add item into cart
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
time.sleep(3)
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
time.sleep(2)
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText
driver.close()








