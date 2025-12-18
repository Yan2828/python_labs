from aiogram import Bot, Dispatcher, executor, types
import config 

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка чего то', 'Покупка чего то конкретно', 'Тип товара (invoice)', config.PAYMENT_TOKEN, 'USD', [types.LabeledPric('Покупка чего то', 5 * 100)]) # 5 долларов=500 монет

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT) #Если успешная оплата
async def success(message: types.Message):
    await message.answer(f'Succes: {message.successful_payment.order_info}') # order_info - информация о платеже (Можно использовать другие команды для ай ди, провйдера и т. д.)
