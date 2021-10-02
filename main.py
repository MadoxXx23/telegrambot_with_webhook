from aiogram import Bot, Dispatcher, executor, types
from flask import Flask, request
import os

server = Flask(__name__)


API_TOKEN = '1014691610:AAFYMsGTMG4uQEbkrsKAiuEALyjD0XHBHcQ'
WEBHOOK_HOST = f'https://webhookl.herokuapp.com/{API_TOKEN}'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 3001


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/Adidas')
    item2 = types.KeyboardButton('/Reebok')
    item3 = types.KeyboardButton('/Adidas')
    item4 = types.KeyboardButton('/Adidas')
    item5 = types.KeyboardButton('/Adidas')
    item6 = types.KeyboardButton('/Adidas')


    markup.add(item1, item2)
    with open('../picture/1.webp', 'rb') as stick:
        await bot.send_sticker(message.chat.id, stick)
    await bot.send_message(message.chat.id,
                           f'Добро пожаловать, {message.from_user.first_name}\nЯ, Loyalty cards бот, создан как тестовый проект\n\nВыберите карту',
                           reply_markup=markup)


@dp.message_handler(commands=['Adidas'])
async def send_adidas(message: types.Message):
    with open('../picture/adidas.webp', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)
    with open('../picture/adidas(cade128).png', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)

@dp.message_handler(commands=['Reebok'])
async def send_adidas(message: types.Message):
    with open('../picture/reebok.webp', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)
    with open('../picture/reebok(cade128).png', 'rb') as picture:
        await bot.send_photo(message.chat.id, picture)

@dp.message_handler(commands=['help'])
async def send_adidas(message: types.Message):
    await bot.send_message(message.chat.id, 'По всём вопросам техничего характера и не только обращаться Telegram - @bel_ous')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Не понял команды')


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
