import requests, telebot
from telebot import types
bot = telebot.TeleBot("6431865078:AAHhPS-hu0MYZ57zoo7Q-c1Z2KXAeUo5je0")
@bot.message_handler(commands=['start'])
def handle_start(message):
    data={'key':'c22d7f5abca4f5ce210049a0fc34fe4a','action':'balance'}
    res=requests.post('https://smmpanel.com/api/v2',data=data).json()
    balance=float(res['balance'])
    views=str(balance/0.0000001).split('.')[0]
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Programer', url="https://t.me/WHI3PER"))
    bot.reply_to(message,f'''- TikTok Views Bot

- Remain : {views} Views

- By : @WHI3PER

- Channel : @old_school_team | @Mods_DZ

- Send Video URL Here''',reply_markup=markup)
def gpt(text) -> str:
 data={'key':'56b29f0e42ee4b057a20fec46d6560e9','action':'add','service':768,'link':text,'quantity':10000}
 res=requests.post('https://smmpanel.com/api/v2',data=data)
 if 'order"' in res.text:
   s='[√] Done Send 10000 Views'
   return s
 else:
  msg=res.json()['error']
  return msg
S = ""
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = gpt(message.text)
    if msg:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Programer', url="https://t.me/WHI3PER"))
        bot.reply_to(message, msg, reply_markup=markup)
    else:
        bot.reply_to(message, "حدث خطأ أعد المحاولة")
print(S)
bot.polling()
