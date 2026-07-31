from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = "8870950829:AAGj8k9l0p1q2w3e4r5t6y7u8i9o0p"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салом! Бот кор мекунад ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
