import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

ele=driver.find_element(By.XPATH, '//*[@id="mySelect"]')
dropdown = Select(ele)
#
# select by index
dropdown.select_by_index(2)
print(dropdown)
time.sleep(2)

# select by value
dropdown.select_by_value('100%')
time.sleep(2)

# # select by visibility of text
# drp.deselect_by_visible_text()
# time.sleep(2)


# capture all the options and print then as a output

# all_options = drp.all_selected_options
#
# for options in all_options:
#     print(options.text)
#
#
# # count the number of dropdown options
# print(len(drp.options))
# time.sleep(3)


# for option in dropdown.options:
#     print(option.text)
#     print(f"{option.get_attribute('value')} : {option.get_attribute('innerHTML')}")
#
#
# # find all the links presents on web page
# elements = driver.find_elements(By.TAG_NAME, 'a')
# for item in elements:
#     print(item.get_attribute('href'))
