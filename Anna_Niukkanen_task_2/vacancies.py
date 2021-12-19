from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# https://hh.ru/search/vacancy?clusters=true&area=1&ored_clusters=true&enable_snippets=true&salary=&text=data+engineer

main_url = 'https://hh.ru'
params = {'clusters': 'true',
          'area': '1',
          'ored_clusters': 'true',
          'enable_snippets': 'true',
          'salary': '0',
          'text': 'data+engineer'
          }

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}

response = requests.get(main_url + '/search/vacancy', params=params, headers=headers)

if response.ok:
    dom = bs(response.text, 'html.parser')
    vacancies = dom.find_all('div', {'class': 'vacancy-serp-item'})

    for vacancy in vacancies:
        name = vacancy.find('a', {'class': 'bloko-link'})
        print()

