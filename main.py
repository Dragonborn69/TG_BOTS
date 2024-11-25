"""import telebot
bot = telebot.TeleBot('7491801885:AAHPhnWTteFVQYRmuzhdIdzALCUfbNqVHac')

name = ''
STAGE = 0

@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    global name
    global STAGE
    if message.text == "/start"  :
            bot.send_message(message.from_user.id, "Привет, как дела?")

    elif message.text.lower() == "нормально":
            bot.send_message(message.from_user.id, "А Я ДУМАЛ СОВА")

    elif message.text == "/help":
            bot.send_message(message.from_user.id, "напиши: /start")

    else:
            a = message.text
            bot.send_message(message.from_user.id, f"я тебя не понимаю твою надпись '{a}' '/help'")
bot.polling(none_stop=True, interval=0)"""


"""import telebot
bot = telebot.TeleBot('')
name = ''
P_color = ''
age = -1
fl_ask = 0

@bot.message_handler(content_types=['text'])

def get_start(message):
    # Глобальные переменные, ты серьезно???? что за убожество
    global fl_ask
    global age
    if message.text == '/start' and fl_ask == 0:
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомися? Напиши да или нет')
        fl_ask = 1
    elif message.text == 'да' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Начнем, как тебя зовут?')
        fl_ask = 0
        age = -1
        bot.register_next_step_handler(message, get_name)
    elif message.text.lower() == 'нет' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Очень жаль! Если захочешь начать общение заново нажми /start')
        fl_ask = 0
    elif fl_ask == 0:
        bot.send_message(message.from_user.id, 'Для начала общения нажми /start')
    elif fl_ask == 1:
        bot.send_message(message.from_user.id, 'Напиши да или нет')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name}, сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == -1:
        if message.text.isdigit():
            age = int(message.text)
            # год надо получить через модуль datetime и от него вычесть возраст

            bot.send_message(message.from_user.id, f'тебя зовут {name}, родился в {2024 - age}')
            bot.send_message(message.from_user.id, f'Подскажи какой цвет ты любишь?')

            bot.register_next_step_handler(message, get_color)
        else:
            bot.send_message(message.from_user.id, 'введите число')

def get_color(message):
    global P_color
    P_color = message.text
    bot.send_message(message.from_user.id, f'Окей теперь я знаю что ты {P_color}')
    bot.send_message(message.from_user.id, 'Показать тебе информацию которую я о тебе знаю?')
    bot.register_next_step_handler(message, Pokaz_info)

# Как же ты ужасно назвал функцию, надо было Show_info
# Учи английский Коля
def Pokaz_info(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id, f'Имя - {name} \n'
                                               f'год рождения - {age}\n'
                                               f'цвет кожи - {P_color} ')
    if message.lower() == 'нет':
        bot.send_message(message.from_user.id, f'Окей, как нибудь в другой раз. До свидания {name}')
        bot.register_next_step_handler(message, get_start)

bot.polling(none_stop=True, interval=0)
"""
"""
import telebot
from telebot import types
from dotenv import load_dotenv  # сначала надо импортировать pip install python-dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))
name = ''
age = -1
fl_ask = 0


@bot.message_handler(content_types=['text'])
def get_start(message):
    global fl_ask
    global age
    age = -1

    if message.text == ('/start' and fl_ask == 0) or ('start' and fl_ask == 0):
        fl_ask = 1
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # наша клавиатура
        key_yes = types.KeyboardButton('да')  # кнопка «Да»
        key_no = types.KeyboardButton('нет')
        keyboard.add(key_yes, key_no)
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомимся?',
                         reply_markup=keyboard)

    elif message.text == 'да' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Начнем, как тебя зовут?', reply_markup=types.ReplyKeyboardRemove())
        fl_ask = 0
        age = -1
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'нет' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Очень жаль! Если захочешь начать общение заново нажми /start',
                         reply_markup=keyboard_start)
        fl_ask = 0
    elif fl_ask == 0:
        bot.send_message(message.from_user.id, 'Для начала общения нажми /start', reply_markup=keyboard_start)
    elif fl_ask == 1:
        bot.send_message(message.from_user.id, 'Напиши да или нет', reply_markup=keyboard)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name}, сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    try:
        age = int(message.text)
        bot.send_message(message.from_user.id, f'тебя зовут {name}, родился в {2024 - age}')
        bot.register_next_step_handler(message, get_start)
    except Exception:
        bot.send_message(message.from_user.id, 'введите число')
        bot.register_next_step_handler(message, get_age)


bot.polling(none_stop=True, interval=0)"""


# This example show how to use inline keyboards and process button presses
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton

TELEGRAM_TOKEN = '7491801885:AAHPhnWTteFVQYRmuzhdIdzALCUfbNqVHac'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
"""
ETAP = 0

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"),
               InlineKeyboardButton("SSSS", callback_data="cb_SSSS"),
               )
    return markup

def gen_markup2():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="Y"),
               InlineKeyboardButton("No", callback_data="N"),
               )
    return markup

def gen_Start():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("START", callback_data="Start"),
               )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global ETAP
    markup = telebot.types.ReplyKeyboardRemove()
    if call.data == "Start":
        ETAP = 0
        bot.send_message(call.message.chat.id, "Yes/no?", reply_markup = gen_markup())

    elif call.data == "cb_yes" and ETAP == 0:
        bot.answer_callback_query(call.id, "Answer is Yes")
        ETAP = 1
    elif call.data == "cb_no" and ETAP == 0:
        bot.answer_callback_query(call.id, "Answer is No")
        ETAP = 1
    elif call.data == "cb_SSSS" and ETAP == 0:
        bot.send_message(call.message.chat.id, "Вернуться к заводским?", reply_markup=gen_markup2())
        ETAP = 1
    elif call.data == "Y" and ETAP == 1:
        bot.send_message(call.message.chat.id, "Нажми старт",reply_markup= keyboard("Start"))
        ETAP = 0
    elif call.data == "N" and ETAP == 1:
        bot.send_message(call.message.chat.id, "Это конец бота, напиши любое сообщение",)
        ETAP = 0

    else:
        bot.send_message(call.message.chat.id, "Нажми Start" , reply_markup=gen_Start())


Knopki = ["Photo", "BIG" , "Video" , "Audio"]

def keyboard(key_type="Start"):
    if key_type == "Start":
        markup = ReplyKeyboardMarkup(row_width=1)
        markup.add(KeyboardButton("START"))
    elif key_type == "Vopr1":
        markup = ReplyKeyboardMarkup(row_width=4)
        Row = [KeyboardButton(i) for i in Knopki]
        markup.add(*Row)
    elif key_type == "A":
        markup = ReplyKeyboardMarkup(row_width=3)
        markup.add(KeyboardButton("Поплакать"))
    elif key_type == "Vopr2":
        markup = ReplyKeyboardMarkup(row_width=3)
        markup.add(KeyboardButton("🎶"),KeyboardButton("🐱‍👤"),KeyboardButton("🐱‍"))


    return markup
"""
"""
@bot.message_handler()
def SETTINGS_MESSAGE(message):
    bot.send_message(message.chat.id, message.photo[0].file_id)
    obratka =  message.photo[0].file_id
    bot.send_photo(message.chat.id, obratka, "Я тоже так могу")
"""


@bot.message_handler(content_types= ['photo'])
def message_handler(message):
    bot.send_message(message.chat.id, 'PHTOT')

@bot.message_handler(content_types= ['text'])
def message_handler(message):
    bot.send_message(message.chat.id, 'TEXT')

@bot.message_handler(content_types= ['voice'])
def message_handler(message):
    bot.send_voice(message.chat.id, message.voice.file_id )




"""    
    if message.text.lower() == "start":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Выбери из 4х" , reply_markup= keyboard("Vopr1"))
    elif message.text.lower() == "big":
        bot.send_message(message.chat.id, "даляю клаву. Напиши как тебя зовут", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)
    elif message.text.lower() == "photo":

        bot.send_photo(message.chat.id,
                       r"https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/b/0/4/b047ac15506f6520266d23828f0b285978b04921.png",
                       "Получите ваше фото")
        file = open("PHOTO2.jfif" , 'rb')
        bot.send_photo(message.chat.id, file , "Фото через Файл")


    elif message.text.lower() == "🎶":
        bot.send_message(message.chat.id, "Удаляю клаву. Какая музыка тебе нрав?",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_music)
    else:
        bot.send_message(message.chat.id, "Нажми старт",reply_markup= keyboard("Start"))

name = ''
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name}, О чем расскажешь дальше?', reply_markup= keyboard("Vopr2") )
music = ''
def get_music(message):
    global music
    music = message.text
    bot.send_message(message.from_user.id, f'сея устал. Тем более ты слушаешь {music}. Вообще больше мне не пиши', reply_markup= keyboard("A") )
"""

bot.infinity_polling()
