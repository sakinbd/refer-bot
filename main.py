from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import BadRequest

CHANNEL_ID = "@freeminingsitebysakin"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text("✅ আপনি চ্যানেলে যোগ দিয়েছেন! স্বাগতম 🎉")
        else:
            await update.message.reply_text(f"🚫 আপনি আমাদের চ্যানেলে জয়েন করেননি!\n👉 প্রথমে জয়েন করুন: {CHANNEL_ID}")
    except BadRequest:
        await update.message.reply_text(f"❗ চ্যানেল চেক করতে ব্যর্থ!\nদয়া করে আগে চ্যানেলে জয়েন করুন:\n{CHANNEL_ID}")

app = ApplicationBuilder().token("7579775071:AAGYmbOSZTiMbed3MnfTzVm6kob3a5eO4q0").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
