"""
Модуль осуществляет запуск бота.
"""

if __name__ == '__main__':
    from bot import Bot
    print('Я запущен!')
    my_bot = Bot()
    my_bot.run()
