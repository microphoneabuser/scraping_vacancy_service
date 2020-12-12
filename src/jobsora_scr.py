import requests
import codecs
from bs4 import BeautifulSoup as BS
import lxml
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
url = 'https://ru.jobsora.com/работа-python-москва'
resp = requests.get(url, headers=headers)
jobs = []
errors = []
if resp.status_code == 200:
    soup = BS(resp.content, 'lxml')
    div_list = soup.find_all('div', attrs={'class':"c-result-item c-main-box c-main-box--hovered js-listing-item js-clickable"})
    if div_list:
        for div in div_list:
            title = div.find('h2')
            print(title.text)
            vac_url = div.find('a', attrs={'class':"c-result-item__title js-wp"})['href']
            company = div.find('span', attrs={'class':"c-result-item__info-item"}).text
            description = div.find('p', attrs={'class':"c-result-item__description"}).text
            jobs.append({'title': title.text, 'url': vac_url, 'descriprion': description, 'company': company})
    else:
        errors.append({'url': url, 'title': "Div does not exist"})
else:
    errors.append({'url': url, 'title': "Page not response"})

h = codecs.open('jobsora.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()