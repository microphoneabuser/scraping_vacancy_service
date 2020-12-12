import requests
import codecs
from bs4 import BeautifulSoup as BS
import lxml


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
h = codecs.open('citys.txt', 'w', 'utf-8')
#city = [306]
for i in range(1, 307):
    url = 'https://hh.ru/search/vacancy?&area=' + str(i) + '&text=Python'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'lxml')
        #city[i] = soup.find('span', attrs={'class':"clusters-value__name"}).text
        s = str(i) + ':'+ soup.find('span', attrs={'class':"clusters-value__name"}).text +'\n'
        h.write(s)
        print(s)

h.close()
