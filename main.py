import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
from logging import basicConfig
from random import choice


async def main():
    await dp.start_polling(bot)


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}!')


@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    await message.answer(f'ID: {message.from_user.id}\nFirst_name: {message.from_user.first_name}\nusername: {message.from_user.username}')


@dp.message(Command('random_pic'))
async def random_pic(message: types.Message):
    num = choice(range(1, 3))
    if num == 1:
        file = types.FSInputFile('images/cat.jfif')
    else:
        file = types.FSInputFile('images/cow.jfif')
    await message.answer_photo(file)


if __name__ == '__main__':
    asyncio.run(main())
