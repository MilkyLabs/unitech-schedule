import asyncio
import datetime
from datetime import date as Date, timedelta as TimeDelta
import sys
import logging
import telegram.formatting as fmt
import telegram.markups as markups
from telegram.commands import *
from repo.repository import Repository
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
    

    await message.answer(f"Hello {html.italic(message.from_user.full_name)}", reply_markup=markups.MAIN_MARKUP)


@dp.message(Command(THIS_WEEK_TIMETABLE_COMMAND))
async def start(message: Message):
    await message.answer(f"{html.code('week command')}", reply_markup=markups.MAIN_MARKUP)


@dp.message(Command(NEXT_WEEK_TIMETABLE_COMMAND))
async def start(message: Message):
    await message.answer(f"{html.code('week command')}", reply_markup=markups.MAIN_MARKUP)


@dp.message(Command(TODAY_TIMETABLE_COMMAND))
async def start(message: Message):
    timetable = Repository().get_day_timetable(Date.today()) 
    answer = fmt.format_day_time_table(timetable)
    await message.answer(answer, reply_markup=markups.MAIN_MARKUP)


@dp.message(Command(TOMORROW_TIMETABLE_COMMAND))
async def start(message: Message):
    timetable = Repository().get_day_timetable(Date.today() + TimeDelta(days=1))
    answer = fmt.format_day_time_table(timetable)
    await message.answer(answer, reply_markup=markups.MAIN_MARKUP)



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
