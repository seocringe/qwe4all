"""
Этот модуль запускает бота в режиме опроса.
"""

import os
# Импортируем модуль django для настройки Django-проекта
import django 
from telegram import Bot # Импортируем класс Bot для работы с Telegram API
from telegram.ext import Updater # Импортируем Updater для обработки входящих обновлений
from dtb.settings import TELEGRAM_TOKEN # Импортируем токен Telegram из настроек проекта
from tgbot.dispatcher import setup_dispatcher # Импортируем функцию для настройки диспетчера

# Задаем переменную окружения, указывающую на файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings') 
django.setup() # Настраиваем Django

def run_polling(tg_token: str = TELEGRAM_TOKEN):
    """ Запустить бота в режиме опроса.

    Аргументы:
        tg_token (str): Токен Telegram, используемый для проверки подлинности бота.

    Возвращает:
        None
    """
    updater = Updater(tg_token, use_context=True)  # Создаем экземпляр Updater для получения обновлений

    dp = updater.dispatcher  # Получаем диспетчер от Updater для управления обработчиками
    dp = setup_dispatcher(dp)  # Настраиваем диспетчер с помощью кастомной функции

    # Получаем информацию о боте и создаем ссылку на него
    bot_info = Bot(tg_token).get_me()  
    bot_link = f"https://t.me/{bot_info['username']}"

    print(f"Получение обновлений для '{bot_link}' началось")  # Выводим сообщение о старте опроса
    # Это может быть полезно для отправки эмодзи разработчику при локальном тестировании
    # bot.send_message(text='👋', chat_id=<ВАШ TELEGRAM ID>)

    updater.start_polling()  # Начинаем опрос серверов Telegram
    updater.idle()  # Запускаем бесконечный цикл приема обновлений

# Этот блок выполнится, если скрипт запущен как главный модуль
if __name__ == "__main__":
    run_polling()
