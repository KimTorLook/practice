#7-6-2
#please ACCEPT COKKIES first, or don't let > button coverd by cookies

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1")

pages_remaining = True
page_num = 1
while pages_remaining:
    # 使用Beautiful Soup剖析HTML網頁
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.select_one("#__next > div.Layout_base__6IeUC.Layout_withSubNav__ByKRF.Layout_justNav__2H4H0 > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti > table") 
    df = pd.read_html(str(table))
    df[0].to_csv("ALL_players_stats" + str(page_num) + ".csv")          # print(df[0].to_csv())
    print("儲存頁面:", page_num)
    try:
        # 自動按下一頁按鈕
        next_link = driver.find_element(By.CSS_SELECTOR, '.Pagination_button__sqGoH+ .Pagination_button__sqGoH') 
        next_link.click()
        time.sleep(5)
        if page_num < 11:
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False  
        
driver.close()