from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from texno_pars import parse_texno
from aiogram.types import Message
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

db = Dispatcher(bot)


@db.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    await message.answer('Salom! Texnomartga ga hush kelibsiz!')
    await show_category_news(message)


async def show_category_news(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Kategoriyani tanlang',
                           reply_markup=buttons_category())


@db.message_handler(content_types=['text'])
async def get_news_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_news = parse_texno(get_value(category_text))

    for news in get_news:
        images = news.get('images')
        cost = news.get('cost')
        title = news.get('title')
        content = news.get('content')
        link = news.get('link')

        await message.answer_photo(photo=images, parse_mode='html', caption=f'''
<b>Narxi: </b> {cost}
<b>Nomlanishi: </b> {title}
<b>Tarifi: </b> {content}''', reply_markup=button_link(link))


executor.start_polling(db)
