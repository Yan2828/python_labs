import telebot
#pip install requests
import requests
import json

bot = telebot.TeleBot('')
API = ''

bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'ВАСАП ма бой, какой твой city')

bot.message_handler(content_types=['start'])
def det_weather(message):
    city = message.text.strip().lower()
    res = requests.det('') # url адрес
    if res.status_code == 200: # 200 - всегда успешная обработка url адреса
        data = json.loads(res.text) # получаем текст и обробатываем в джейсон и лоадс
        temp = data["main"]["temp"]
        bot.peply_to(message, f'Сейчас погода: {temp}') #res.json() - не читаемый (["main"]["temp"] - обращение к нужному термену)

        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')

bot.polling(none_stop=True)