#7-6-1a    20221219
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://hahow.in/courses"
driver.get(url)

items = driver.find_elements(By.CSS_SELECTOR, "h4, .title")  #debug
                                            
for item in items:
    print(item.text)                    

driver.quit()