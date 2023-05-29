from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//button[text() = 'Start']").click()

element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')

print(f"Message : {element.get_attribute('innerHTML')}")

time.sleep(5)


# implicitly_wait