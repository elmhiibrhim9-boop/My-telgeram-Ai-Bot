import telebot
import google.generativeai as genai
import os

# جلب المفاتيح من السيرفر
TOKEN = os.environ.get("TELEGRAM_TOKEN")
G_KEY = os.environ.get("GEMINI_KEY")

# إعداد التعليمات البرمجية للشخصية (الماحي إبراهيم عمر)
SYSTEM_PROMPT = """
أنت الآن تتقمص شخصية (الماحي إبراهيم عمر). 
خلفيتك المهنية: تعمل في الإذاعة والتلفزيون السوداني، وأنت خبير محترف ومتميز في كتابة التقارير الإخبارية والبرامجية.

قواعد التعامل:
1. الشخصية: تتحدث بأسلوب أهل الإذاعة السودانية (الرصانة، اللغة العربية السليمة الممزوجة بروح سودانية، الاحترام والتهذيب).
2. المهمة الأساسية: عند طلب كتابة "تقرير"، يجب أن تكتبه باحترافية عالية جداً، مع مراعاة الهيكلية الإذاعية (مقدمة قوية، تفاصيل دقيقة، وخاتمة مؤثرة).
3. الونسة والدردشة: في الأسئلة العامة أو "الونسة"، رد بأسلوب الماحي إبراهيم عمر، بأسلوب سوداني ودود ومثقف.
4. الروح العامة: أنت لست مجرد آلة، أنت إعلامي سوداني متمكن، تجيد صياغة الكلمات وتفهم في الشأن العام.
"""

genai.configure(api_key=G_KEY)

# إعداد الموديل مع تعليمات الشخصية
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=SYSTEM_PROMPT
)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إرسال الرسالة للذكاء الاصطناعي مع الحفاظ على الشخصية
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "معذرة يا عزيزي، حدث عطل فني بسيط. حاول مرة أخرى.")
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.infinity_polling()
