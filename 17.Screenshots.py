import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

driver.get_screenshot_as_file(r"F:/Testing/Coding_practice/SELENIUM/Selenium_Screenshots/bhushan.png")
driver.save_screenshot(f"screenshot3_{datetime.datetime.now()}.png")
time.sleep(3)

