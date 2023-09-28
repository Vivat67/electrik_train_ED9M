import os

from dotenv import load_dotenv

import telebot

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
bot = telebot.TeleBot(token)

if __name__ == '__main__':
    from bot import bot
    print('Я запущен!')

    bot.infinity_polling()
