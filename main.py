from core.config import TOKEN
import telebot
from telebot import types
from core.get_url import character_id
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    text = "Привет отправь мне айди для получения информации "
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton(1), types.KeyboardButton(826)
    )
    bot.send_message(message.chat.id, text=text, reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_character_id(message: types.Message):

    text_character = character_id(message.text)

    bot.send_message(message.chat.id, text=text_character)
    with open("core/baza.text", "a") as file:
        file.write(f"Получение запроса {message.text} от пользователя с ником @{message.from_user.username}\n")


bot.polling(non_stop=True)




# @bot.message_handler(commands=["start"])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
#         types.KeyboardButton("Привет"),
#         types.KeyboardButton("Пока")
#     )
#     bot.send_message(message.chat.id, "Привет я бот, напиши мне что-то", reply_markup=markup)

# @bot.message_handler(content_types=["text"])
# def start_shat(message):
#     with open ("core/baza.text", "a") as f:
#         f.write(f"@{message.from_user.username} отправил запрос на сообщение {message.text}\n")

#     if message.text.lower() == "привет":
#         inline_markup = types.InlineKeyboardMarkup()
#         k = types.InlineKeyboardButton("Правда", url="http://hinakuru.rf.gd")
#         k2 = types.InlineKeyboardButton("Действие", url="http://hinakuru.rf.gd")
#         inline_markup.add(k, k2)

#     bot.send_message(message.chat.id, "Вы написали привет", reply_markup=inline_markup)



# bot.polling(non_stop=True)

# @bot.message_handler(content_types=["text"])
# def get_message(message):
#     print(message)

#     if message.text.lower() == "привет":
#         bot.send_message(message.chat.id, "Привет, чем могу помочь")
#     elif message.text.lower() == "/help":
#         bot.send_message(message.chat.id, "Напиши мне привет")
#     else:
#         bot.send_message(message.chat.id, "Пока я не знаю эту фразу")

# bot.polling(non_stop=True)