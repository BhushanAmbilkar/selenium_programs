import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

fileInput = driver.find_element(By.ID, 'file-upload')
button = driver.find_element(By.ID, 'file-submit')

fileInput.send_keys(r"F:\New_Volume_(F)\Desktop-Pictures\Quotefancy-2010506-3840x2160.jpg")
button.click()



