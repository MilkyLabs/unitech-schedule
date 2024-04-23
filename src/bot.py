import asyncio
import datetime
import sys
import logging
import telegram.formatting as fmt
import parser.time_table as tt
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = [[
        KeyboardButton(text="/на_сегодня"),
        KeyboardButton(text="/на_неделю"),
        KeyboardButton(text="/на_завтра"),
    ]]
    markup = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите команду")

    await message.answer(f"Hello {html.italic(message.from_user.full_name)}", reply_markup=markup)


@dp.message(Command("на_неделю"))
async def start(message: Message):
    await message.answer(f"{html.code('week command')}")


@dp.message(Command("на_сегодня"))
async def start(message: Message):
    time_table = tt.get_time_table()['days'][datetime.date.today().weekday()]
    answer = fmt.format_day_time_table(time_table)
    await message.answer(answer) 

@dp.message(Command("на_завтра"))
async def start(message: Message):
    time_table = tt.get_time_table()['days'][datetime.date.today().weekday() + 1] # TODO: fix index out of range error
    answer = fmt.format_day_time_table(time_table)
    await message.answer(answer)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
