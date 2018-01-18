from telegram.ext import Updater, CommandHandler

token = "498370125:AAHnCOBNJldxxvn2vHKNJAjjy0u7-nDLwWU"


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
