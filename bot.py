from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils.exceptions import Throttled
from flask import Flask, request
import os
server = Flask(__name__)
storage = MemoryStorage()
API_TOKEN = os.environ['API_TOKEN']
WEBHOOK_HOST = f'195.2.73.23/{API_TOKEN}'
WEBHOOK_PATH = '/home'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '195.2.73.23'  # or ip
WEBAPP_PORT = 3001

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

@server.route('/' + API_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = types.Update.as_json(json_string)
    dp.process_update(update)

@server.route('/')
def webhook():
    bot.delete_webhook()
    bot.set_webhook(url=WEBHOOK_HOST)
    return "!", 200

@dp.message_handler(commands=['text'])
async def anti_flood(message: types.Message, *args, **kwargs):
    await bot.send_message(message.chat.id, 'Наша программа слишком медленная, чтоб угнаться за вами. Пусть поспит немного...')
    await asyncio.sleep(3)


@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=1)
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/Adidas')
    item2 = types.KeyboardButton('/Reebok')
    item3 = types.KeyboardButton('/Adidas')
    item4 = types.KeyboardButton('/Adidas')
    item5 = types.KeyboardButton('/Adidas')
    item6 = types.KeyboardButton('/Adidas')


    markup.add(item1, item2)
    with open('./picture/1.webp', 'rb') as stick:
        await bot.send_sticker(message.chat.id, stick)
    await bot.send_message(message.chat.id,
                           f'Добро пожаловать, {message.from_user.first_name}\nЯ, Loyalty cards бот, создан как тестовый проект\n\nВыберите карту',
                           reply_markup=markup)


@dp.message_handler(commands=['Adidas'])
@dp.throttled(anti_flood, rate=1)
async def send_adidas(message: types.Message):
    with open('./picture/adidas.webp', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)
    with open('./picture/adidas(cade128).png', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)

@dp.message_handler(commands=['Reebok'])
@dp.throttled(anti_flood, rate=1)
async def send_adidas(message: types.Message):
    with open('./picture/reebok.webp', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)
    with open('./picture/reebok(cade128).png', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)

@dp.message_handler(commands=['help'])
@dp.throttled(anti_flood, rate=3)
async def send_adidas(message: types.Message):
    await bot.send_message(message.chat.id, 'По всём вопросам техничего характера и не только обращаться Telegram - @bel_ous')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Не понял команды')

#
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

    # insert code here to run it after start


async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass

if __name__ == '__main__':
    # server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    # executor.start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH, on_startup=on_startup, on_shutdown=on_shutdown,
    #               skip_updates=True, host=WEBAPP_HOST, port=WEBAPP_PORT)
    executor.start_polling(dp, skip_updates=True)
#fdfsdfsdfsdfsd