import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def parse_gazeta(category):
    load_dotenv()
    list_news = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='nblock')

    for block in blocks[:3]:
        images = block.find('img', class_='lazy').get('data-src')
        date_time = block.find('div', class_='ndt').get_text().split()[0:2]
        title = block.find('h3').get_text().split()
        content = block.find('p').get_text().split()
        link = HOST + block.find('a').get('href')
        list_news.append({
            'images': images,
            'date_time': date_time,
            'title': title,
            'content': content,
            'link': link
        })
    return list_news


parse_gazeta('society/')