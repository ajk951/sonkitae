from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://duckduckgo.com/?q='+'&iar=images&iax=images&ia=images'
plusurl = input("검색어를 입력하세요.")
url = baseUrl + quote_plus(plusurl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgUlr = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUlr)

print("다운로드 완료")