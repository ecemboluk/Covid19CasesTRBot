""" Python Telegram Chatbot About Covi19 Cases in Turkey"""

# Libraries
import requests
from telegram.ext import Updater, CommandHandler, CallbackContext
from bs4 import BeautifulSoup


# Web Scraping
def connectHealthDepartmentSite():
    r = requests.get('https://www.worldometers.info/coronavirus/country/turkey/')
    source = BeautifulSoup(r.text, "lxml")
    cases = source.find("li", attrs={"class": "news_li"}).text
    case_list = [i for i in cases.split(" ")]
    case_text = "Today in Turkey, number of new cases are " + case_list[0] + " and number of new deaths are " + \
                case_list[4] + "."
    return case_text


# Sent case numbers as message.
def case_scraping(update: Updater, context: CallbackContext):
    update.message.reply_text(connectHealthDepartmentSite())


# Start bot
def main():
    # Create Updater object and attach dispatcher to it
    TOKEN = "1888765913:AAEX741SGbgo6pqgl3fbkvWT6wl8wrl3OsE"
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handler to dispatcher
    start_handler = CommandHandler('case', case_scraping)
    dispatcher.add_handler(start_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
