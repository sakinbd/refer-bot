from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import BadRequest

# বাধ্যতামূলক চ্যানেল
CHANNEL_ID = "@freeminingsitebysakin"

# রেফারাল ডেটা রাখার জন্য
user_referrals = {}

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "unknown"
    args = context.args

    # 1️⃣ চ্যানেল মেম্বারশিপ চেক
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status not in ["member", "administrator", "creator"]:
            await update.message.reply_text(f"🚫 আপনি এখনও চ্যানেলে জয়েন করেননি!\n👉 জয়েন করুন: https://t.me/{CHANNEL_ID[1:]}")
            return
    except BadRequest:
        await update.message.reply_text(f"❗ চ্যানেল চেক করতে সমস্যা হচ্ছে। দয়া করে জয়েন করুন: https://t.me/{CHANNEL_ID[1:]}")
        return

    # 2️⃣ রেফার চেক
    if args:
        referrer_id = args[0]
        if referrer_id != str(user_id):
            if referrer_id not in user_referrals:
                user_referrals[referrer_id] = set()
            user_referrals[referrer_id].add(user_id)

    # 3️⃣ মেসেজ পাঠাও
    await update.message.reply_text(
        f"👋 হ্যালো {username}, স্বাগতম!\n\n"
        f"✅ আপনি সফলভাবে বট ব্যবহার শুরু করেছেন।\n\n"
        f"📢 এখন আপনার রেফার লিংক:\n"
        f"https://t.me/{context.bot.username}?start={user_id}\n\n"
        f"🎯 ৫ জনকে রেফার করলে পাবেন ২০ টাকা ফ্লেক্সিলোড!\n"
        f"২৫ জনে ৫০ টাকা, ৫০ জনে ১০০ টাকা!\n\n"
        f"🎁 Extra বোনাস:\n"
        f"HGNICE: https://hgnice.bet/#/register?invitationCode=35466896884\n"
        f"DKWIN: https://dkwin9.com/#/register?invitationCode=25574112576\n"
        f"💬 ১০০ টাকা ডিপোজিট করে যোগাযোগ করুন: @Sakin9520"
    )

    # 4️⃣ রেফার কাউন্ট জানাও
    referrals = user_referrals.get(str(user_id), set())
    await update.message.reply_text(f"📊 আপনি এখন পর্যন্ত {len(referrals)} জনকে রেফার করেছেন।")

# Bot Setup
app = ApplicationBuilder().token("7579775071:AAGYmbOSZTiMbed3MnfTzVm6kob3a5eO4q0").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
