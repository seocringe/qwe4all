"""
This module provides a function to run a bot in polling mode.
"""

from telegram.ext import Updater
from dtb.settings import TELEGRAM_TOKEN
from tgbot.dispatcher import setup_dispatcher


class SpecificException(Exception):
    """
    This is a specific exception class.
    """


def run_polling(tg_token=None):
    """Run bot in polling mode."""
    if tg_token is None:
        tg_token = TELEGRAM_TOKEN

    try:
        updater = Updater(token=str(tg_token), use_context=True)
        setup_dispatcher(updater.dispatcher)
        print(
            "Polling of 'https://t.me/"
            + updater.bot.get_me()["username"].strip()
            + "' has started"
        )
        updater.start_polling()
        updater.idle()
    except SpecificException as error:
        print(f"A specific error occurred: {error}")


if __name__ == "__main__":
    run_polling()
