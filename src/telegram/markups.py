from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.commands import *
from aiogram.filters import CommandStart


main_buttons = [[
    KeyboardButton(text=f"/{TODAY_TIMETABLE_COMMAND}"),
    KeyboardButton(text=f"/{TOMORROW_TIMETABLE_COMMAND}"),
], [
    KeyboardButton(text=f"/{THIS_WEEK_TIMETABLE_COMMAND}"),
    KeyboardButton(text=f"/{NEXT_WEEK_TIMETABLE_COMMAND}"),
],[
    KeyboardButton(text=f"/{SETTINGS_COMMAND}"),
]]

settings_buttons = [[
    KeyboardButton(text=f"/enable_notification"),
    KeyboardButton(text=f"/{TOMORROW_TIMETABLE_COMMAND}"),
], [
    KeyboardButton(text=f"/{THIS_WEEK_TIMETABLE_COMMAND}"),
    KeyboardButton(text=f"/{NEXT_WEEK_TIMETABLE_COMMAND}"),
],[
    KeyboardButton(text=f"/{CommandStart()}"),
]]

MAIN_MARKUP = ReplyKeyboardMarkup(
        keyboard=main_buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите команду")

SETTINGS_MARKUP = ReplyKeyboardMarkup(
        keyboard=settings_buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите команду")
