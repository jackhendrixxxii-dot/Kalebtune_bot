# deploy trigger
# force deploy
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙏 Welcome to KalebTune Bot\nSend me the name of the mezmur, artist or audio.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()
    
    # Translate phonetic Amharic to Amharic
    translated = translator.translate(user_input, dest='am').text.lower()

    for title, data in mezmur_db.items():
        if title in user_input or title in translated:
            response = f"🎶 *{title.title()}* by *{data['artist']}*"
            if "lyrics" in user_input or "lyric" in user_input:
                response += f"\n📜 Lyrics:\n{data['lyrics']}"
            await update.message.reply_text(response, parse_mode='Markdown')
            return

    await update.message.reply_text("🙏 Sorry, I couldn't find the mezmur. Try another name.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

print("Bot is running...")
app.run_polling()
