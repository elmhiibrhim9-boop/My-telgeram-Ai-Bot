import telebot
import google.generativeai as genai
import os

# جلب المفاتيح من إعدادات السيرفر
TOKEN = os.environ.get("TELEGRAM_TOKEN")
G_KEY = os.environ.get("GEMINI_KEY")

# إعداد الذكاء الاصطناعي
genai.configure(api_key=G_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except:
        bot.reply_to(message, "حدث خطأ بسيط، حاول مجدداً.")

if __name__ == "__main__":
    bot.infinity_polling()
