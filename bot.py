from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import wikipedia

wikipedia.set_lang("uz")
TOKEN = "8518085777:AAHi3FJLcBDK2sMDd78xdFwWen8iBt9UZlw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men AI Wikipedia botman. Menga mavzu yozing.Bot @Javohir_Writes ga tegishli.")

async def wiki_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    try:
        result = wikipedia.summary(query, sentences=3)
        await update.message.reply_text(result)
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(f"Bu mavzu bir nechta variantga ega: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("Bunday sahifa topilmadi.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, wiki_search))
    app.run_polling()

if __name__ == "__main__":
    main()