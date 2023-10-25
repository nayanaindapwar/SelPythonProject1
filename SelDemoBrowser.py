# First Selenium Program to launch the browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# For Chrome Browser by using the downloaded local chrome driver
# service_obj = Service("/home/nayana/PycharmProjects/MyTestProject/drivers/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# Firefox driver - Firefox browser
# service_obj = Service()
# driver = webdriver.Firefox(service=service_obj)

# For Firefox Browser by using the downloaded local gecko driver
# service_obj = Service("/home/nayana/PycharmProjects/MyTestProject/drivers/geckodriver")
# driver = webdriver.Firefox(service=service_obj)


# Edge Driver - Edge browser
# service_obj = Service()
# driver = webdriver.Edge(service=service_obj)

# For Edge Browser by using the downloaded local edge driver
# service_obj = Service("/home/nayana/PycharmProjects/MyTestProject/drivers/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://courses.rahulshettyacademy.com/courses")
print(driver.current_url)
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()







