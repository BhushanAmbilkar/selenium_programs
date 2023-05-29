from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

print(f"Page Title : ", driver.title)
print(f"Page URL : ", driver.current_url)
print(driver.service)



