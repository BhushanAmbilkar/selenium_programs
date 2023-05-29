import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

parentDiv = driver.find_element(By.ID, 'myDropdown')
ele = driver.find_element(By.ID, 'dropOption2')

actionObj = ActionChains(driver)
actionObj.move_to_element(parentDiv).move_to_element(ele).click().perform()
time.sleep(3)

ele = driver.find_element(By.ID, 'myButton')
actionObj.click(ele).perform()
time.sleep(3)

actionObj.context_click().perform()
time.sleep(3)

# actionObj.context_click(ele).perform()
# time.sleep(3)
