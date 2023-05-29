import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email" ).clear()
driver.find_element(By.NAME, "email").send_keys("bhushan@gmail.com")

driver.find_element(By.NAME, "pass").clear()
driver.find_element(By.NAME, "pass").send_keys("9562jlkol")

driver.find_element(By.NAME, "login").click()
time.sleep(10)