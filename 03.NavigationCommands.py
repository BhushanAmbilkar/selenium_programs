import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

print(f"Page title : ", driver.title)
time.sleep(2)

driver.get("https://www.youtube.com")

print(f"Page title :", driver.title)
time.sleep(2)

driver.back()
time.sleep(2)
print(f"Page URL : ", driver.current_url)


driver.forward()
time.sleep(2)
print(f"Page URL : ", driver.current_url)



