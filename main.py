from telebot import TeleBot
from config import TOKEN
from telebot import types

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id, "Assalomu alaykum!")



print("bot ishga tushdi")
bot.infinity_polling()