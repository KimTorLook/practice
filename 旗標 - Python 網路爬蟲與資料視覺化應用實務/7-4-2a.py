#7-4-2a

from selenium import webdriver
import os
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
html_path = "file:///" +os.path.abspath("Ch7_4.html")
driver.implicitly_wait(10)
driver.get(html_path)

#7_4_2
form = driver.find_element(By.ID, "loginForm")
print(form.tag_name)
print(form.get_attribute("id"))

#a
user = driver.find_element(By.NAME,"username")
print(user.tag_name)
print(user.get_attribute("type"))

eles = driver.find_elements(By.NAME,"continue")
for ele in eles:
    print(ele.get_attribute("type"))
driver.quit()