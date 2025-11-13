import telebot 
import webbrowser
from telebot import types # -> разрешение отправки разного типа файла

bot = telebot.TeleBot('8181403411:AAEKQIqEyiob0ZEzNP0_tmZ-y11bObUb5AQ')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    s = types.InlineKeyboardMarkup()
    f1 = types.InlineKeyboardButton('Перейти на сайт погоды', url = 'https://yandex.ru/pogoda/ru/moscow?lat=55.559898&lon=37.583839') # InlineKeyboardButton -> один из видов кнопок
    s.row(f1) 
    f2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
    f3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
    s.row(f2, f3) # row() -> сколько кнопак в ряд (add -> добавить по умолчанию)
    bot.reply_to(message, 'Красивое фото, но лучше посмотри на кнопки', reply_markup=s)

@bot.callback_query_handler(func=lambda callback: True) # bot.callback_query_handler обращение к callback_data
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('И зачем ты изменил тект', callback.message.chat.id, callback.message.message_id)
 

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://yandex.ru/pogoda/ru/moscow')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Твой ID: {message.from_user.id}")
'''
ID: {message.from_user.id}
👤 Имя: {message.from_user.first_name}
📝 Фамилия: {message.from_user.last_name}
📛 Username: @{message.from_user.username}
💬 Язык: {message.from_user.language_code}
👥 ID чата: {message.chat.id}
'''

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<u><b>Себастьян</b></u>, <em>иди учиться!</em>', parse_mode='html') # parse_mode='html' используется для корректировки текста
'''
<b> - жирный
<em> - курсивом
<u> - подчеркивание
'''
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Твой секрет это твой ID -> {message.from_user.id}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Твой ID: {message.from_user.id}') # bot.reply_to -> ответ на предыдущие сообщение пользователя
'''
метод @bot.message_handler() должен находиться внизу,
(если мы не используем определенные команды) 
инече не будут выполнятся последующие команды
'''

bot.polling(none_stop=True) # можно использовать bot.infinity_polling() -> программа выпорлняется без остановки 

# Чтобы остановить код -> ctrl + C