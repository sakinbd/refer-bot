from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! 🎉")

app app = ApplicationBuilder().token("7579775071:AAGYmbOSZTiMbed3MnfTzVm6kob3a5eO4q0").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
