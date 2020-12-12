import requests
import codecs
from bs4 import BeautifulSoup as BS
import lxml
from random import randint

__all__ = ('jobsora_parsing', 'hh_parsing')

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.57',
    'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Accept': 'text/html,appllication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]


url_hh = 'https://hh.ru/search/vacancy?area=35&text=Python'

url_jobsora = 'https://ru.jobsora.com/работа-python-москва'

def jobsora_parsing(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 4)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'lxml')
            div_list = soup.find_all('div', attrs={'class':"c-result-item c-main-box c-main-box--hovered js-listing-item js-clickable"})
            if div_list:
                for div in div_list:
                    title = div.find('h2')
                    vac_url = div.find('a', attrs={'class':"c-result-item__title js-wp"})['href']
                    company = div.find('span', attrs={'class':"c-result-item__info-item"}).text.replace(",", "")
                    description = div.find('p', attrs={'class':"c-result-item__description"}).text
                    jobs.append({'title': title.text, 'url': vac_url, 'description': description, 'company': company, 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exist"})
        else:
            errors.append({'url': url, 'title': "Page not response"})

    return jobs, errors


def hh_parsing(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 4)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'lxml')
            div_list = soup.find_all('div', attrs={'class':"vacancy-serp-item"})
            if div_list:
                for div in div_list:
                    title = div.find('a', attrs={'class':"bloko-link HH-LinkModifier"})
                    vac_url = title['href']
                    description = div.find('div', attrs={'data-qa':"vacancy-serp__vacancy_snippet_responsibility"}).text + ' ' +div.find('div', attrs={'data-qa':"vacancy-serp__vacancy_snippet_requirement"}).text
                    company = div.find('a', attrs={'class':"bloko-link bloko-link_secondary"}).text
                    jobs.append({'title': title.text, 'url': vac_url, 'description': description, 'company': company, 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exist"})
        else:
            errors.append({'url': url, 'title': "Page not response"})

    return jobs, errors

#print(jobsora_parsing(url_jobsora))
#print(hh_parsing(url_hh))