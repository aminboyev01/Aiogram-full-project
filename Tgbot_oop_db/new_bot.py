import telebot

# Tokenni shu yerga yozing
bot = telebot.TeleBot("8443731531:AAF2X8d3_PhKakjkiorRULmIlLZqRLyUxZY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom, Shohrux! 👋 Men sizning birinchi botingizman!")
    bot.send_message(message.chat.id,"Sizga qanday yordam bera olaman?")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

print("Bot ishga tushdi...")
bot.polling()
