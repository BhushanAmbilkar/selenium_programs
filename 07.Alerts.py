import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

## Js alert
ele = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
ele.click()
time.sleep(3)

driver.switch_to.alert.accept()
time.sleep(3)


## JS confirm
# ele = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button')
# ele.click()
# time.sleep(2)
#
# driver.switch_to.alert.accept()
# time.sleep(3)
#
# driver.switch_to.alert.dismiss()
# time.sleep(3)


## Js prompt
ele = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button')
ele.click()
time.sleep(3)

alert = driver.switch_to.alert
alert.send_keys("Bhushan Ambilkar")
time.sleep(3)
alert.accept()
time.sleep(3)

