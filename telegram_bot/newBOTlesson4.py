import telebot 
import sqlite3 # база данных

bot = telebot.Telebot('8181403411:AAEKQIqEyiob0ZEzNP0_tmZ-y11bObUb5AQ')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('project.sql') # файл, котрый будет хранить базу данных (sql -> расширенние файла)
    cur = conn.cursor() # вызываем курсор для работы с базой данных

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_incerment primary key, name varchar(50), pass varchar(50))') # Создаем таблицу для пользователья, если ее не существет (имя, пароль). id int auto_incerment primary key - ключ по умолчанию


bot.infinity_polling()
