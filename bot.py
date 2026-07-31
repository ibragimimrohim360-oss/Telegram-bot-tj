import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салом! Ман AI Promt Master TJ ҳастам ✅\nЧӣ кӯмак лозим?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Шумо навиштед: {message.text}")

print("Бот кор мекунад...")
bot.polling()
