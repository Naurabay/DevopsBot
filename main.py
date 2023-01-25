import telebot
from local_settings import *  

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text) 
    bot.send_message(message.chat.id, "I'm a bot, please talk to me more!\nBot by @naurabay")

bot.infinity_polling()