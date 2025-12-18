from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.PeplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открвть веб страницу'), web_app=WebAppInfo(url = '')) # WebAppInfo - устанавливаем класс, url = '' - адрес страницы
    await message.answer('Привет, ма бой', reply_markup=markup)


executor.start_polling(dp)