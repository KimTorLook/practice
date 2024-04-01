#7-4-2c

from selenium import webdriver
import os
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
html_path = "file:///" +os.path.abspath("Ch7_4.html")
driver.implicitly_wait(10)
driver.get(html_path)
link1 = driver.find_element(By.LINK_TEXT, 'Continue')
print(link1.text)
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
print(link2.text)
link3 = driver.find_element(By.LINK_TEXT, '取消')
print(link3.text)
link4 = driver.find_element(By.PARTIAL_LINK_TEXT, '取')
print(link4.text)

h3 = driver.find_element(By.TAG_NAME, "h3")   #7-4-2d
print(h3.text)
p = driver.find_element(By.TAG_NAME, "p")
print(p.text)

content=driver.find_element(By.CLASS_NAME, "content") #7-4-2e
print(content.text)
driver.quit()