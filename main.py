from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from googletrans import Translator
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

translator = Translator()

mezmur_db = {
    "yesus new egziabher": {
        "artist": "Solomon",
        "lyrics": "ኢየሱስ ነው እግዚአብሔር...\nዘንድሮም አይቀየርም"
    },
    "kidane mehret": {
        "artist": "Martha",
        "lyrics": "እመቤታችን ኪዳነ ምሕረት..."
    }
}

async def start(update: Update, context:
    text = update.message.text.lower()

    if "mesfin" in text or "getachew" in text:
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("songs/mesfin_getachew.mp3", "rb"))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't recognize that mezmur yet.")

    await update.message.reply_text("🙏 Sorry, I couldn't find the mezmur. Try another name.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

print("Bot is running...")
app.run_polling()
