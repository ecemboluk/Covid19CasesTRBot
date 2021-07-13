import requests
import os
from telegram.ext import Updater, CommandHandler, CallbackContext
from bs4 import BeautifulSoup

PORT = int(os.environ.get('PORT', 5000))


def connectHealthDepartmantSite():
    r = requests.get('https://www.worldometers.info/coronavirus/country/turkey/')
    source = BeautifulSoup(r.text, "lxml")
    cases = source.find("li", attrs={"class": "news_li"}).text
    case_list = [i for i in cases.split(" ")]
    case_text = "Today in Turkey, number of new cases are " + case_list[0] + " and number of new deaths are " + \
                case_list[4] + "."
    return case_text


def start(update: Updater, context: CallbackContext):
    update.message.reply_text(connectHealthDepartmantSite())


def main():
    # Create Updater object and attach dispatcher to it
    TOKEN = "1888765913:AAEX741SGbgo6pqgl3fbkvWT6wl8wrl3OsE"
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    print("Bot started")

    # Add command handler to dispatcher
    start_handler = CommandHandler('case', start)
    dispatcher.add_handler(start_handler)

    # Start the bot
    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://covid19casestrbot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
