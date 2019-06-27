import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/search?q=apple+iphone+6s&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_2&otracker1=AS_Query_HistoryAutoSuggest_0_2&as-pos=0&as-type=HISTORY&as-backfill=on')
# print(http)
# lxml - library xml
page = bs4.BeautifulSoup(http,'lxml')
# print(page)
div = page.find('div', class_='_3wU53n')
print(div.text)

price = page.find('div', class_='_1vC4OE')
print(price.text)