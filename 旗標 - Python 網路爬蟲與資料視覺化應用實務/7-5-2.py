#7-5-2

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.github.com/login"
driver.get(url)


username="xxxxxxxxxxxxxxxxxx@gmail.com"
password="PASSWORD!"

userfield = driver.find_element(By.CSS_SELECTOR, "#login_field")
passwordfield = driver.find_element(By.CSS_SELECTOR, "#password")

userfield.send_keys(username)
passwordfield.send_keys(password)

submitbutton = driver.find_element(By.CSS_SELECTOR, ".js-sign-in-button")
submitbutton.click()

items = driver.find_elements(By.CSS_SELECTOR, '#global-nav')

for item in items:
    print(item.text)
    print(item.get_attribute("a.href"))   #unknow error
    
driver.quit()