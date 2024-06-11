from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from gazeta_pars import pars_gazeta
from aiogram.types import Message

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

db = Dispatcher(bot)


@db.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    await message.answer('Salom! GAzeta ga hush kelibsiz!')


executor.start_polling(db)
