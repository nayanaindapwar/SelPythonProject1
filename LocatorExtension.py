# Locator Extension
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
time.sleep(5)

# XPATH using tags
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)

# CSS Selector using tags
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
time.sleep(2)

# CSS Selector
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").submit()

# XPATH using text attribute for the same above button
# driver.find_element(By.XPATH, "//button[@text() = 'Save New Password']").submit()




