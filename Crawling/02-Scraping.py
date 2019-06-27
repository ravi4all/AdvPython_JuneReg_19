import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/search?q=apple+iphone+6s&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_2&otracker1=AS_Query_HistoryAutoSuggest_0_2&as-pos=0&as-type=HISTORY&as-backfill=on')

page = bs4.BeautifulSoup(http,'lxml')
divList = page.find_all('div', class_='_3wU53n')
# for item in divList:
#     print(item.text)

priceList = page.find_all('div', class_='_1vC4OE _2rQ-NK')
# for item in priceList:
#     print(item.text)
# print(len(divList), len(priceList))

ratingList = page.find_all('div',class_='hGSR34')

for i in range(len(priceList)):
    print(divList[i].text)
    print(priceList[i].text, "Rating :",ratingList[i].text)
    print("##################")