import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

ele = driver.find_element(By.ID,'readOnlyText')

print(f"Value : {ele.get_attribute('value')}")
print(f"Type : {ele.get_attribute('type')}")
print(f"Name : {ele.get_attribute('name')}")
print(f"ID : {ele.get_attribute('id')}")























import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

driver.maximize_window()

ele = driver.find_element(By.ID, 'myTextInput2')

print(f"Value : { ele.get_attribute('value')}")
print(f"Type : {ele.get_attribute('type')}")
print(f"Name : {ele.get_attribute('name')}")
print(f"ID : {ele.get_attribute('id')}")

time.sleep(10)