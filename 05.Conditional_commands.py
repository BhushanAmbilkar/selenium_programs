import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
#
# # is_displayed
# ele = driver.find_element(By.ID, 'dropOption1')
# print(f"Is element displayed : {ele.is_displayed()}")
#
# ele = driver.find_element(By.ID, 'myButton')
# print(f"Is element displayed : {ele.is_displayed()}")
#
# # is_selected
# ele = driver.find_element(By.ID, 'radioButton1')
# print(f"is element selected : {ele.is_selected()}")
#
# ele = driver.find_element(By.ID, 'radioButton2')
# print(f"is element selected : {ele.is_selected()}")

#  # is_enabled
driver.get("https://www.geeksforgeeks.org/")
# get element
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[1]/span')
# print value
print(element.is_enabled())
#

 # conditional commands
 # .is_selected
 # .is_displayed
 # .is_enabled


