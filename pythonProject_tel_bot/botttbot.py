from PIL import Image
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import io

YOUR_BOT_TOKEN = '6708257802:AAH9w014Bb5itMFvYCoEyu4oIsTyj0VaaP0'

bot = Bot(token=YOUR_BOT_TOKEN)
dp = Dispatcher(bot)

async def download_and_process_image(image_url):
    # Загружаем изображение из интернета
    response = requests.get(image_url)

    if response.status_code == 200:
        # Открываем изображение с помощью Pillow
        image = Image.open(io.BytesIO(response.content))

        # Уменьшаем размер изображения в два раза
        resized_image = image.resize((image.width // 2, image.height // 2))

        # Сохраняем уменьшенное изображение в байтах
        output_buffer = io.BytesIO()
        resized_image.save(output_buffer, format='JPEG')
        output_buffer.seek(0)

        return output_buffer
    else:
        raise Exception(f"Не удалось загрузить изображение. Код статуса: {response.status_code}")

@dp.message_handler(lambda message: message.text.startswith('http'))
async def process_image_url(message: types.Message):
    image_url = message.text

    try:
        image_bytes = await download_and_process_image(image_url)

        # Отправляем уменьшенное изображение обратно пользователю
        await bot.send_photo(message.chat.id, photo=image_bytes)
    except Exception as e:
        await bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)