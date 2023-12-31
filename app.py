import telebot
from config import BotToken, keys
from extensions import *

bot = telebot.TeleBot(BotToken)


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


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def rejection(message: telebot.types.Message):

    text = 'Данный бот работает только с текстом!'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        arq = message.text.split()
        if len(arq) != 3:
            raise APIException('Неверное количество параметров!')

        quote, base, amount = arq
        total_base = ValuesConverter.get_prise(quote, base, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base}: {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
