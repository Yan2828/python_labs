# установить библиотеку pip install CurrencyConverter
import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.Telebot('')

currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, введите сумму')
        bot.register_next_step_handler(message, summa) # следущая функцию, которую ввидет пользователь это summa
        return
    
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2) # В одном ряду максимум две кнопки
        f1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        f2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        f3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        f4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(f1, f2, f3, f4)
        bot.send_message(message.chat.id, 'Выберете пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше за 0. Впишите заново число')
        bot.register_next_step_handler(message, summa)

@bot.callback_querty_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/') # В data будет находиться текст upper - верхний регистор split - разделить некую строку по символу /
        res = currency.convert(amount, values[0], values[1]) # Функция convert позволяет выполнить конвертацию
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму') # round позволяет округлить знаки после запятой (в данном случае 2)
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, f'Ввидите пару знчений через слеш')
        bot.register_next_step_handler(call.message, mycurrency)

def mycurrency(message):
    try:
        values = message.text.upper().split('/') 
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception: # Обрабатываем глобальный класс Exception
        bot.send_message(message.chat.id, f'Что-то не так.Впишите значение заново')
        bot.register_next_step_handler(message, mycurrency)

