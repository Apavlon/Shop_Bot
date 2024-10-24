from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("7718156608:AAFVwr5UPrzA_uBl7q33JaRMcL3LMEukwdI")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):

    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton("Открыть веб страницу",
               web_app=WebAppInfo(url="https://apavlon.github.io/Shop/")))

    await message.answer("Привет, друг!", reply_markup=markup)
