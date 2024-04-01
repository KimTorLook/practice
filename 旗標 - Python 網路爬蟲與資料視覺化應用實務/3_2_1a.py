#Ch3_2_1a

import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.yahoo.com.hk")   #invalid link instead
r.encoding="utf8"
soup=BeautifulSoup(r.text,"lxml")
print(soup)