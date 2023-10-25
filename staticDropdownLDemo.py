import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://codenboxautomationlab.com/registration-form/")

driver.find_element(By.NAME,"fname").send_keys("Jay")
driver.find_element(By.NAME,"lname").send_keys("Arora")
driver.find_element(By.NAME,"email").send_keys("jay.arora@gmail.com")
courseDropdown = Select(driver.find_element(By.ID, "nf-field-22"))
courseDropdown.select_by_visible_text("Selenium Automation")
monthDropdown = Select(driver.find_element(By.ID, "nf-field-24"))
monthDropdown.select_by_visible_text("December")
time.sleep(5)
monthDropdown.select_by_index(1)
time.sleep(5)









