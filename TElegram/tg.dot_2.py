# 5469652432:AAEOo10g5nRQWIngokOj_Y7I6ZdE9jbOvXc
import telebot
from telebot import types

token = "5469652432:AAEOo10g5nRQWIngokOj_Y7I6ZdE9jbOvXc"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, "Что будем делать?")
    markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    help = types.KeyboardButton("/help")
    markup_start.add(help)
    bot.send_message(message.chat.id, 'Тут ты найдёшь список всех команд', reply_markup=markup_start)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    study = types.KeyboardButton("/обучение")
    Calc = types.KeyboardButton("/calc")

    markup.add(study, Calc)
    bot.send_message(message.chat.id, "Что посмотрим?", reply_markup=markup)


@bot.message_handler(commands=['обучение'])
def study(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Overone", url="https://overone.by"))
    img = open("overone.png", "rb")
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.send_message(message.chat.id, "Тут я начал изучать программирование", reply_markup=markup)


value = ""
old_value = ""

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                telebot.types.InlineKeyboardButton("C", callback_data="C"),
                telebot.types.InlineKeyboardButton("<=", callback_data="<="),
                telebot.types.InlineKeyboardButton("/", callback_data="/") )

keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data="7"),
                telebot.types.InlineKeyboardButton("8", callback_data="8"),
                telebot.types.InlineKeyboardButton("9", callback_data="9"),
                telebot.types.InlineKeyboardButton("*", callback_data="*") )

keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data="4"),
                telebot.types.InlineKeyboardButton("5", callback_data="5"),
                telebot.types.InlineKeyboardButton("6", callback_data="6"),
                telebot.types.InlineKeyboardButton("-", callback_data="-") )

keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data="1"),
                telebot.types.InlineKeyboardButton("2", callback_data="2"),
                telebot.types.InlineKeyboardButton("3", callback_data="3"),
                telebot.types.InlineKeyboardButton("+", callback_data="+") )

keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                telebot.types.InlineKeyboardButton("0", callback_data="0"),
                telebot.types.InlineKeyboardButton(",", callback_data="."),
                telebot.types.InlineKeyboardButton("=", callback_data="=") )

@bot.message_handler(commands = ["start", "calc"] )
def getmessage(message):
    global value
    if value == "":
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == "no" :
        pass
    elif data == "C" :
        value = ""
    elif data == "=" :
        try:
            value = str(eval(value))
        except:
            value = "Ошибка!"
    else:
        value += data

    if value != old_value:
        if value == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)

    old_value = value
    if value == "Ошибка!": value = ""







if __name__ == "__main__":
    bot.polling(none_stop=True)
