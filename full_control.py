import telebot
TOKEN = '8644104939:AAHsP_64XxEOg6-J2okdlp02jqQX_dKlqd0'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Remote Control Active!")
bot.polling()
