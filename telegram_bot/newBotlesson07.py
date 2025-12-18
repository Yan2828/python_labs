from aiogram import Bot, Dispatcher, executor, types

bot = Bot('8181403411:AAEKQIqEyiob0ZEzNP0_tmZ-y11bObUb5AQ')

dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo']) #ommands=['start'] (content_types обрабатывает любой текст)
async def start(message: types.Message): # Используется принцп асинхроности, поэтому async (types -> тип этого параметра message)
    # await bot.send_message(message.chat.id, "Hello")
    # await message.answer('Hello') # Используем, так как async(метод answer выполняет тоже самое, что send_message)
    await message.reply('Hello') # тоже самое await message.answer('Hello')
    file = open('/some.png', 'rb') # открываем этот файл
    await message.answer_photo(file) # тип файла

@dp.message_handler() #ommands=['start'] (content_types обрабатывает любой текст)
async def info(message: types.Message): 
    markup = types.InlineKeyboardMarkup() #row_width= скольколько кнопок в одном ряду (указывать в скобках в этой строке)
    markup.add(types.InlineKeyboardButton('Site', url=''))
    markup.add(types.InlineKeyboardButton('Site', url=''))
               


executor.start_polling(dp) # программа работает постоянно answer