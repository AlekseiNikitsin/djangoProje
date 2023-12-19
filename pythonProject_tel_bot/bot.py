import asyncio
import logging
import time
from asyncio import Lock
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.types import InputFile
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from PIL import Image, ImageFont, ImageDraw
sample = Image.open('r2.jpg')
logging.basicConfig(level=logging.INFO)
type(sample)
bot = Bot(token="6710094945:AAE5aFoDaL62qz-Z8uSoWGDr-iYuskljvwg")
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler()
async def start(message: types.Message):
    if message.text == '/start':
        return await message.answer(text = 'Здраствуйте \n,как вас зовут')
    if message.text == 'Привет':
        return await message.reply(text='Здраствуй')

    await message.answer(text='Здравствуйте!\nКак Вас зовут?')
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):
    await message.photo[-1].download('r1.png')
    time.sleep(1)
    sample = Image.open('r1.png')
    font = ImageFont.truetype('Minecraft.otf', size=104, encoding='ASCII')
    draw = ImageDraw.Draw(sample)
    draw.text((50, 200), font=font, text="Hello world", align="center", fill='blue')
    sample.save('r3.png')
    sample1 = Image.open('r1.png')
    font1 = ImageFont.truetype('tahoma.ttf', size=54, encoding='ASCII')
    draw1 = ImageDraw.Draw(sample1)
    draw1.text((20, 50), font=font1, text="Hello world", align="center", fill='blue')
    sample1.save('r2.png')
    await message.answer_photo(InputFile('r3.png'))
    await message.answer_photo(InputFile('r2.png'))



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    #Base.metadata.create_all(engine)
    asyncio.run(main())