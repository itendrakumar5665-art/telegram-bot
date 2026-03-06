from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8682978181:AAEc4zBM6X3gQYULBLTuEM5W8PdBX6XlPHU"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Itendra Rewards Bot 🎉")


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Your Points: 0")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("balance", balance))

app.run_polling()
