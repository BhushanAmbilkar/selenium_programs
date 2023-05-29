import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, '//*[@id="start"]/button' ).click()

time.sleep(5)

locator = (By.XPATH,'//*[@id="finish"]/h4')
element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
print(f"Message : {element.get_attribute('innerHTML')}")

time.sleep(5)

