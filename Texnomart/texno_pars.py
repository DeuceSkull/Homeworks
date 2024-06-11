import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def parse_texno(category):
    load_dotenv()
    list_news = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='product-item-component')

    for block in blocks[:5]:
        images = block.find('img', class_='product-image').get('data-src')
        cost = block.find('div', class_='product-price__current').get_text()
        title = block.find('a', class_='product-name f-14 c-373 mb-1 768:mb-2 btn-link w-normal').get_text()
        link = HOST + block.find('a').get('href')
        list_news.append({
            'images': images,
            'date_time': cost,
            'title': title,
            'link': link
        })
    return list_news


parse_texno('telefony/')
