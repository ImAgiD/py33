'28.02.24=================Telebot================='
# CTRL + C когда меняем что-то
import telebot, wikipedia
from telebot import types

token = '7057690013:AAGGdracX1ONkq5PV9DPybL2mRMdQUEYrtc'
bot = telebot.TeleBot(token) 

wikipedia.set_lang('ru')

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Меню')
button2 = types.KeyboardButton("Выход") 
keyboard.add(button1,button2)

@bot.message_handler(commands =['start'])
def start(message):
    message2 = bot.send_message(message.chat.id, 'Привет! Я поисковик. Напиши любое слово', reply_markup = keyboard)
    bot.register_next_step_handler(message2, handle_text)

def getwiki(word):
    try:
        wikitext = wikipedia.page(word).content[:500]
        wikitext = wikitext.split('. ')
        wikitext = '. '.join(wikitext[:-1]) + '.'
        print(wikitext)
    except:
        wikitext = 'Об этом слове  нет информации'
    return wikitext 
    
def handle_text(message):
    word = message.text
    info = getwiki(word)
    bot.send_message(message.chat.id, info, reply_markup=types.ReplyKeyboardRemove())
    
bot.polling(none_stop=True)
