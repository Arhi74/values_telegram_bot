import telebot
from bot_token import BotToken

bot = telebot.TeleBot(BotToken)


@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello!')


bot.polling()
