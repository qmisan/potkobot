import json
import requests
from telegram.ext import Updater, CommandHandler

# Globals
token = "498370125:AAHnCOBNJldxxvn2vHKNJAjjy0u7-nDLwWU"
coin_market_cap_api_url = "https://api.coinmarketcap.com/v1/ticker/"


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def iota(bot, update):
    suffix = "iota/"
    response = requests.get(coin_market_cap_api_url + suffix)
    json_data = json.loads(response.text)
    update.message.reply_text("Ei hätää pojat raketoi ihan just ;)\n" +
                              "IOTA = {0} USD".format(json_data[0]["price_usd"]))


def bitcoin(bot, update):
    suffix = "bitcoin/"
    response = requests.get(coin_market_cap_api_url + suffix)
    json_data = json.loads(response.text)
    update.message.reply_text("Ai että bitcoin fanboy ;)\n" +
                              "BTC = {0} USD".format(json_data[0]["price_usd"]))


def lauri(bot, update):
    update.message.reply_text("Suomen humaanein viestijä!")


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('iota', iota))
updater.dispatcher.add_handler(CommandHandler('bitcoin', bitcoin))
updater.dispatcher.add_handler(CommandHandler('lauri', lauri))

updater.start_polling(poll_interval=1)
# updater.idle()
