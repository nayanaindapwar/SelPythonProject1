import time  # Java Script Executor

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Running the script in headless browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options= chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Scrolling down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)
# Taking screenshot
driver.get_screenshot_as_file("screen.png")


