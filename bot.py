from telebot import *
from mindai import *
from types import *
bot = TeleBot("6696024805:AAGzVeaJIp6SzVH3CSviKGiLKU5RHN16PCw")
#توكن بوتك 
@bot.message_handler(commands=['start'])
def start(message):
    userm = message.from_user.username
    nam = message.from_user.full_name
    name_pro = message.from_user
    key = types.InlineKeyboardMarkup()
    bot1 = types.InlineKeyboardButton('- Dev ' ,url ='https://t.me/FIood_1500')
    bot2 = types.InlineKeyboardButton('- Channel ' ,url ='https://t.me/ToGoLang')
    key.add(bot1,bot2)
    p1ng = "https://t.me/ToGoLang/9"
    bot.send_photo(message.chat.id,p1ng,f"""<strong>
- ᥕ𝖾𝗅ᥴ᥆𝗆𝖾 Ꭵᥒ 𝖻᥆𝗍 🇮🇶, @{userm}
- {nam} 𝗍α𝗅𝗄 𝗍᥆ 𝗍h𝖾 𝖻᥆𝗍 Ꭵᥒ 𝖾ᥒ𝗀𝗅Ꭵ𝗌h , 
</strong>""",parse_mode="html",reply_markup=key)
@bot.message_handler(func=lambda message: True)
def main(message):
    x = Ai().chat(message=message.text)
    bot.reply_to(message,x['reply'])
bot.infinity_polling()
