import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
url = 'https://editorial.rottentomatoes.com/guide/best-sci-fi-movies-of-all-time/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
result={}

critics = [a.text for a in soup.find_all('div', attrs={'class': 'info critics-consensus'}) if a]
title = [a.text for a in (d.find("h2").find("a") for d in soup.find_all('div', attrs={'class': 'col-sm-18 col-full-xs countdown-item-content'})) if a]
#リストに空きの項目があったので削除する
title.remove("")
title.remove("The Day of the Triffids")
title.remove("When Worlds Collide")
for x in range(len(title)):
    result[title[x]] = critics[x]

#csvとして出力する
df = pd.json_normalize(result)
df=df.T
print(df)
df.to_csv("sf150.csv",encoding="utf-8")