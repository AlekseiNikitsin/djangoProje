import asyncio
import logging
from asyncio import Lock
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(text='/start')
async def start(message: types.Message):

    await message.answer(text='Здравствуйте!\nКак Вас зовут?')



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    #Base.metadata.create_all(engine)
    asyncio.run(main())
