import urllib.request as url
import bs4

http = url.urlopen('https://www.marvel.com/')
page = bs4.BeautifulSoup(http)

images = page.find_all('img')
imgSrc = []
for i in range(len(images)):
    imageUrl = images[i]['src']
    url.urlretrieve(imageUrl, 'img_{}.jpg'.format(i))