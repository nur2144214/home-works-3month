from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

cancel_button = KeyboardButton('отмена')
cancel.add(cancel_button)

def size_keyboard():
    """Создаем клавиатуру с кнопками размеров."""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    sizes = ["S", "M", "L", "XL", "XXL"]
    buttons = [types.KeyboardButton(text=size) for size in sizes]
    keyboard.add(*buttons)
    return keyboard