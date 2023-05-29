import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'Click Here').click()

h3element = driver.find_element(By.TAG_NAME, 'h3')
print(f"H3 content : {h3element.get_attribute('innerHTML')}")

# need to switch to new_window()
print(" window handles :- ", driver.window_handles)
print("Before switch window :- ", driver.current_window_handle )
print("Before switch title :- ", driver.title)

all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
print(" all handles [-1] :- ", all_handles[-1])
print("After switch window :- ", driver.current_window_handle)
print("After switch title :- ", driver.title)

# this will switch to newly opened window
h3element = driver.find_element(By.TAG_NAME, 'h3')
print(f"Newly opened window content : {h3element.get_attribute('innerHTML')}")
time.sleep(2)
