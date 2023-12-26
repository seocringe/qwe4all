"""
Этот модуль запускает бота в режиме опроса.
"""

import os

# Импортируем модуль django для настройки Django-проекта
import django
from telegram import Bot  # Импортируем класс Bot для работы с Telegram API

# Импортируем Updater для обработки входящих обновлений
from telegram.ext import Updater

# Импортируем токен Telegram из настроек проекта
from dtb.settings import TELEGRAM_TOKEN

# Импортируем функцию для настройки диспетчера
from tgbot.dispatcher import setup_dispatcher

# Задаем переменную окружения, указывающую на файл настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dtb.settings")
django.setup()  # Настраиваем Django


def run_polling(tg_token: str = TELEGRAM_TOKEN):
    """Запустить бота в режиме опроса.

    Аргументы:
        tg_token (str): Токен Telegram, используемый для проверки подлинности бота.

    Возвращает:
        None
    """
    from telegram.ext import Dispatcher  # Import the Dispatcher class

    from telegram.ext import Dispatcher  # Import the Dispatcher class

    updater = Updater(
        tg_token, use_context=True
    )  # Create an instance of Updater to receive updates

    # Specify the type of "dispatcher" as "Dispatcher"
    dp: Dispatcher = updater.dispatcher
    # Configure the dispatcher using the custom function
    dp = setup_dispatcher(dp)

    # Get bot information and create a link to it
    bot_info = Bot(tg_token).get_me()
    bot_link = f"https://t.me/{bot_info['username']}"

    # Выводим сообщение о старте опроса
    print(f"Получение обновлений для '{bot_link}' началось")
    # Это может быть полезно для отправки эмодзи разработчику при локальном тестировании
    # bot.send_message(text='👋', chat_id=<ВАШ TELEGRAM ID>)

    updater.start_polling()  # Начинаем опрос серверов Telegram
    updater.idle()  # Запускаем бесконечный цикл приема обновлений


# Этот блок выполнится, если скрипт запущен как главный модуль
if __name__ == "__main__":
    run_polling()
