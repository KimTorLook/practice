#7-4-2b
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome("./chromedriver")
html_path = "file:///" +os.path.abspath("Ch7_4.html")
driver.implicitly_wait(10)
driver.get(html_path)
# 定位<form>標籤
form1 = driver.find_element(By.XPATH, "/html/body/form[1]")
print(form1.tag_name)
form2 = driver.find_element(By.XPATH, "//form[1]")
print(form2.tag_name)
form3 = driver.find_element(By.XPATH, "//form[@id='loginForm']")
print(form3.tag_name)
# 定位密碼欄位
pwd1 = driver.find_element(By.XPATH, "//form/input[2][@name='password']")
print(pwd1.get_attribute("type"))
pwd2 = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[2]")
print(pwd2.get_attribute("type"))
pwd3 = driver.find_element(By.XPATH, "//input[@name='password']")
print(pwd3.get_attribute("type"))
# 定位清除按鈕
clear1 = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
print(clear1.get_attribute("type"))
clear2 = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")
print(clear2.get_attribute("type"))
driver.quit()