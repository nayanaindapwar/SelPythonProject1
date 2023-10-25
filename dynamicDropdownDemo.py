import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.refresh()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "india":
        country.click()
        time.sleep(5)
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "ind"

