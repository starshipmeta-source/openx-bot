from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8498004352:AAEjwHTe7nkqkZJyfgJqmcVKPhKkydty0Sg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("openx bot is alive 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
