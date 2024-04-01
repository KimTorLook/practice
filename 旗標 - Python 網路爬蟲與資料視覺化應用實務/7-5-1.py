#7-5-1  20221214

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.google.com"
driver.get(url)

keyword = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
keyword.send_keys("XPath")
keyword.send_keys(Keys.ENTER)

items = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']")

for item in items:
    h3 = item.find_element(By.TAG_NAME,"h3")
    print(h3.text)
    a = item.find_element(By.TAG_NAME, "a")   
    print(a.get_attribute("href"))
    
driver.quit()