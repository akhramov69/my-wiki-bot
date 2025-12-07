# bot.py
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import wikipedia

# -----------------------------
# Token va kanal linkini Environment variable orqali olamiz
TOKEN = os.environ.get("8518085777:AAHi3FJLcBDK2sMDd78xdFwWen8iBt9UZlw")  # Render’da TOKEN nomli Environment variable qo‘shing
CHANNEL_LINK = "https://t.me/Javohir_Writes"  # Bu yerga o‘z kanal linkingizni qo‘ying
# -----------------------------

# Wikipedia tilini o'rnatamiz (uzbekcha)
wikipedia.set_lang("uz")

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men Wikipedia botman. Menga mavzu yozing va men sizga qisqacha ma'lumot beraman."
    )

# /help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Siz shunchaki mavzu yozing va men Wikipedia’dan ma’lumot beraman.\n"
        "Masalan: Python, O‘zbekiston, Futbol"
    )

# Foydalanuvchi matn yozganda ishlaydigan funksiya
async def wiki_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    try:
        # Wikipedia sahifasini olish
        page = wikipedia.page(query)
        # Birinchi 1000 belgini olish (ko‘p matn uchun oshirish mumkin)
        text = page.content[:1000]
        # Manba va kanal qo‘shish
        message = f"{text}\n\nManba: {page.url}\n\n📢 Bizning kanal: {Javohir_Writes}"
        await update.message.reply_text(message)
    except wikipedia.exceptions.DisambiguationError as e:
        options = ', '.join(e.options[:5])
        await update.message.reply_text(f"Bu mavzu bir nechta variantga ega: {options}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("Bunday sahifa topilmadi.")

# -----------------------------
# Botni ishga tushirish
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, wiki_search))
    app.run_polling()

if __name__ == "__main__":
    main()
