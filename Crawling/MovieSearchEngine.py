import bs4
import urllib.request as url

path = "https://www.flipkart.com/mi-led-smart-tv-4a-pro-80-cm-32-android/p/itmfdwh5jyqhmvzg?pid=TVSFDWH5K9N2FDTK&srno=s_1_1&otracker=search&otracker1=search&lid=LSTTVSFDWH5K9N2FDTK9CAPYS&fm=SEARCH&iid=6533b6d4-6bf3-4833-a245-8378ef24e319.TVSFDWH5K9N2FDTK.SEARCH&ppt=sp&ppn=sp&ssid=6xybfe8qm80000001561639472228&qH=c9a1fdac6e082dd8"
http = url.urlopen(path)

page_1 = bs4.BeautifulSoup(http, 'lxml')
div = page_1.find('div', class_='col _39LH-M')
a_tag = div.find_all('a')
# print(a_tag[-1]['href'])
for i in range(10):
    path_2 = 'https://www.flipkart.com' + a_tag[-1]['href'] + '&page={}'.format(i+1)
    http = url.urlopen(path_2)
    page_2 = bs4.BeautifulSoup(http,'lxml')

    reviewList = page_2.find_all('p', class_='_2xg6Ul')
    # ratingList = page_2.find_all('div', class_='hGSR34 E_uFuv')
    ratingDiv = page_2.find_all('div', class_='col _390CkK _1gY8H-')
    ratings = []
    for i in range(len(ratingDiv)):
        ratingList = ratingDiv[i].find('div', class_='hGSR34')
        ratings.append(ratingList.text)
    # print(len(ratingList))
    # print(len(reviewList), len(ratings))
    # for data in ratingList:
    #     print(data)
    for i in range(len(ratings)):
        print("Review :",reviewList[i].text)
        print("Rating :",ratings[i])
    print("#########")