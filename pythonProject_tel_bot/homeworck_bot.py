import sqlite3
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

YOUR_BOT_TOKEN = '6710094945:AAEV9VbPhH5XMFefxM9rq2wyZLza8Pd8a8w'

# Инициализация базы данных
conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')
cursor.executemany("INSERT INTO products (name) VALUES (?)", [("Товар 1",), ("Товар 2",), ("Товар 3",)])
conn.commit()

bot = Bot(token=YOUR_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Получаем товары из базы данных
    cursor.execute("SELECT name FROM products")
    products = [product[0] for product in cursor.fetchall()]

    buttons = [types.KeyboardButton(product) for product in products]
    keyboard.add(*buttons)

    await message.answer("Выберите товар:", reply_markup=keyboard)


@dp.message_handler(
    lambda message: message.text in [product[0] for product in cursor.execute("SELECT name FROM products")])
async def handle_product_choice(message: types.Message):
    chosen_product = message.text
    await message.answer(f"Вы выбрали товар: {chosen_product}")
@dp.message_handler(text='фото')
async def cmd_start(message: types.Message):
    await message.answer_photo(
     photo='https://catherineasquithgallery.com/uploads/posts/2021-02/1614282221_80-p-chernii-fon-laika-98.jpg',
       caption='фото из интернета')


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)