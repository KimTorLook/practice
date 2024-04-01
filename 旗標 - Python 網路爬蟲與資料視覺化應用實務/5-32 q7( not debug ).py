#5-32 q7( not debug )

from bs4 import BeautifulSoup
from bs4.element import NavigableString

fp=open("index.html", 'r', encoding='utf-8')

soup=BeautifulSoup(fp,'lxml')
tag_li=soup.find(class_="nav-item")
tag_ul=tag_li.parent
for child in tag_ul.contents:
    if not isinstance(child, NavigableString):
        print(child)            #唔知個練習想要乜 maybe  print(child.a.string)
fp.closed