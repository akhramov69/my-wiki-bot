import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import wikipedia

# Telegram token Render'dan olinadi
TOKEN = os.environ.get("TOKEN")

# Kanal reklama linki
CHANNEL_LINK = "https://t.me/Javohir_Writes"

wikipedia.set_lang("uz")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Wikipedia botman.\nMenga mavzu yoz, men batafsil ma'lumot beraman."
    )

async def wiki_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    try:
        page = wikipedia.page(query)
        text = page.content[:1200]  # ko‘proq ma’lumot
        message = (
            f"{text}\n\n"
            f"🔗 Manba: {page.url}\n"
            f"📢 Kanal: {Javohir_Writes}"
        )
        await update.message.reply_text(message)
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(
            "Bir nechta variant bor:\n" + ", ".join(e.options[:5])
        )
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("Bunday sahifa topilmadi.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, wiki_search))
    app.run_polling()

if __name__ == "__main__":
    main()
