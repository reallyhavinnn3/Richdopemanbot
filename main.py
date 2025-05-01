import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random
import datetime

BOT_NAME = "RichYoungin3xBot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Welcome to {BOT_NAME}! Ask me to predict anything: sports, crypto, lotto, horoscopes, or casino outcomes.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args) if context.args else "something"
    response = generate_prediction(query)
    await update.message.reply_text(response)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    response = generate_prediction(query)
    await update.message.reply_text(response)

def generate_prediction(query):
    predictions = [
        "Team X will win by 2 points.",
        "Bitcoin will rise 3.2% in the next 24 hours.",
        "Capricorn: Today is your lucky day to play cards.",
        "You have a 7 in 10 chance of hitting the jackpot today.",
        "Your crypto pick: ETH over BTC this week."
    ]
    return (
        f"Prediction for: {query}
"
        f"Pick: {random.choice(predictions)}
"
        f"Confidence: {random.randint(85, 99)}%
"
        f"Reason: Based on pattern analysis and fictional expert insight.
"
        f"Timestamp: {datetime.datetime.now()}"
    )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
