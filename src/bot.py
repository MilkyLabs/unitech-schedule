import asyncio
import datetime
import sys
import logging
import parser.time_table as tt
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message


BOT_TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello {html.italic(message.from_user.full_name)}") 


@dp.message(Command("week"))
async def start(message: Message):
    await message.answer(f"{html.code('week command')}") 


@dp.message(Command("today"))
async def start(message: Message):
    time_table = tt.get_time_table()['days'][datetime.date.today().weekday()]
    answer =f"Расписание на {html.bold(time_table['date'])}\n\n"
    for lesson in time_table['lessons']:
        answer += f"* {lesson['number']}-я пара {lesson['subject']} {html.italic(lesson['room'] + ' каб.')}\n"
    await message.answer(answer) 


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
