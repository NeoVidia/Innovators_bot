from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Функция для отправки сообщения "Привет" с кнопкой
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Привет", callback_data="greet")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет", reply_markup=reply_markup)

# Функция для обработки нажатия на кнопку
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("Привет", callback_data="greet")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Привет", reply_markup=reply_markup)

# Основная функция для запуска бота
def main():
    # Замени 'YOUR_BOT_TOKEN' на токен своего бота
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
