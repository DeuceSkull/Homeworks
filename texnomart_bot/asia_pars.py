import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_asia(category):
    load_dotenv()
    list_news = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    }
    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='category__item')
    # print(blocks)

    for block in blocks[:3]:
        content = block.find('div', class_='category__content')
        link = HOST + block.find('a').get('href')
        title = block.find('h2').get_text().split()

        list_news.append({
            'content': content,
            'link': link,
            'title': title
        })
        return list_news


pars_asia('katalog/noutbuki/')
