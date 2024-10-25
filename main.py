from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json


bot = Bot("7718156608:AAFVwr5UPrzA_uBl7q33JaRMcL3LMEukwdI")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Открыть веб страницу",
               web_app=WebAppInfo(url="https://apavlon.github.io/Shop/")))

    await message.answer("Привет, друг!", reply_markup=markup)


@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')

executor.start_polling(dp)
