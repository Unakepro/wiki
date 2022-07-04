from telebot import TeleBot
from config import TOKEN
from bs4 import BeautifulSoup
import requests

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Enter name of wiki page: ")


@bot.message_handler(content_types=['text'])
def parse(message):
    print(message.text)
    soup = BeautifulSoup(requests.get(f"https://en.wikipedia.org/wiki/{message.text}").text, 'html.parser')
    items = soup.find_all('p')
    for i in items:
        try:
            bot.send_message(message.chat.id, i.getText())
        except BaseException:
            pass


bot.polling()
