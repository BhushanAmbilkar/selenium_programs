import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element(By.ID, 'box3')
target = driver.find_element(By.ID, 'box103')

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(2)

source1 = driver.find_element(By.ID, 'box6')
target1 = driver.find_element(By.ID, 'box106')

action = ActionChains(driver)
action.drag_and_drop(source1, target1).perform()