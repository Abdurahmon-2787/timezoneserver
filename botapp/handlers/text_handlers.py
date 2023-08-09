from telebot.types import Message, ReplyKeyboardRemove

from store.models import Category, Product
from ..loader import bot
from ..keyboards import *


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alaykum, Timezone botimimizga hush kelibsiz",
                     reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == 'Menu⌚️')
def reaction_register(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = "Kechirasiz, siz ro'yxatdan o'tmagansiz. Iltimos buyurtma berish uchun ro'yxatdan o'ting!"
    markup = register_btn()

    bot.send_message(chat_id, text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Ro'yxatdan o'tish 📝")
def reaction_register(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.set_state(user_id, chat_id)
    bot.send_message(chat_id, "Ism familiyangizni kiriting: ", reply_markup=ReplyKeyboardRemove())



# @bot.message_handler(func=lambda message: message.text in [category.title for category in Category.objects.filter(parent=None)])
# def reaction_category(message: Message):
#     chat_id = message.chat.id
#     category = Category.objects.get(title=message.text)
#     bot.send_message(chat_id, f"{message.text.capitalize()}",
#                      reply_markup=get_btn([category.title for category in Category.objects.filter(parent=category)]))
#



