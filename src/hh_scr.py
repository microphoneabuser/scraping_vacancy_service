import requests
import codecs
from bs4 import BeautifulSoup as BS
import lxml


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
#domain = 'https://hh.ru'
url = 'https://hh.ru/search/vacancy?area=35&text=Python'
resp = requests.get(url, headers=headers)
jobs = []
errors = []
if resp.status_code == 200:
    soup = BS(resp.content, 'lxml')
    #main_div = soup.find('div', attrs={'class':"vacancy-serp"})
    div_list = soup.find_all('div', attrs={'class':"vacancy-serp-item"})
    if div_list:
        for div in div_list:
            title = div.find('a', attrs={'class':"bloko-link HH-LinkModifier"})
            #print(title.text)
            vac_url = title['href']
            #print(vac_url)
            company = div.find('a', attrs={'class':"bloko-link bloko-link_secondary"}).text
            description = div.find('div', attrs={'data-qa':"vacancy-serp__vacancy_snippet_responsibility"}).text + ' ' +div.find('div', attrs={'data-qa':"vacancy-serp__vacancy_snippet_requirement"}).text
            jobs.append({'title': title.text, 'url': vac_url, 'descriprion': description, 'company': company})
    else:
        errors.append({'url': url, 'title': "Div does not exist"})
else:
    errors.append({'url': url, 'title': "Page not response"})

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()