# 抓Dcard清華大學版的文章標題

import urllib.request as req
url = "https://www.dcard.tw/f/nthu"
request = req.Request(url, headers = {
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("h2", class_="tgn9uw-2 jWUdzO")
with open("dcard.txt", mode="w", encoding="utf-8") as file:
    for title in titles:
        file.write(title.a.string+"\n")
