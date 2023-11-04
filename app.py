import telebot
from bot_token import BotToken

bot = telebot.TeleBot(BotToken)

keys = {'доллар': 'USD'}


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Чтобы начать работу с ботом введите команду в следующем формате:\n <имя валюты> <имя валюты, \
в какую надо перевести> <количество>\nНапример: рубль доллар 100\
\nДля вывода списка валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split()


bot.polling()
