import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("person abc")
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abc@123")
driver.find_element(By.ID, "exampleCheck1").click()
# Shortcuts for CSS Selector --> #id, .classname
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

# CSS Selector : //tagname[@attribute = 'value'] --> //input[@type = 'submit']
driver.find_element(By.XPATH, "//input[@type = 'submit']").submit()
time.sleep(5)
message =driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message



