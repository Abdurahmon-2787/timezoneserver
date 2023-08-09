from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def register_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Ro'yxatdan o'tish📝 "))
    return markup


def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("Menu⌚️"), KeyboardButton("Savat🛒 "),
        KeyboardButton("Sozlamalar⚙️ "), KeyboardButton("Aloqa📞"),
        KeyboardButton("Zakazlar tarixi📁")
    )
    return markup


def get_btn(lst: list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for item in lst:
        markup.add(KeyboardButton(item))
        return markup

