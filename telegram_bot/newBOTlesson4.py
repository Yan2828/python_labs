import telebot 
import sqlite3 # база данных
name = None

bot = telebot.TeleBot('8181403411:AAEKQIqEyiob0ZEzNP0_tmZ-y11bObUb5AQ')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('project.sql') # файл, котрый будет хранить базу данных (sql -> расширенние файла)
    cur = conn.cursor() # вызываем курсор для работы с базой данных

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_incerment primary key, name varchar(50), pass varchar(50))') # Создаем таблицу для пользователья, если ее не существет (имя, пароль). id int auto_incerment primary key - ключ по умолчанию
    conn.commit() # выполнить создание таблицы, чтобы была добавлина в базу данных (синхранизирует)
    cur.close() # Закрываем соединение курсора (базу данных)
    conn.close() # Само соединение

    bot.send_message(message.id.chat, 'Сейчас тебя зарегаем, бро, введи свой ник')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.id.chat, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('project.sql') # файл, котрый будет хранить базу данных (sql -> расширенние файла)
    cur = conn.cursor() # вызываем курсор для работы с базой данных

    cur.execute(f'INSERT INTO users(name, pass) VALUES ("%s", "%s")' %(name, password)) # задаем в самом начале переменную name, так как в это й функции ее нет
    # %s - какие то значения, %(name, password) - будем указывать эти значения 
    conn.commit() # выполнить создание таблицы, чтобы была добавлина в базу данных (синхранизирует)
    cur.close() # Закрываем соединение курсора (базу данных)
    conn.close() # Само соединение

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='list'))

    bot.send_message(message.id.chat, 'Зареган', reply_parameters='')

@bot.callback_query_handler(func=lambda call: True) # True если не будет значения
def callback(call):
    conn = sqlite3.connect ('ithroger sql')
    cur = conn.cursor()

    cur.execute( 'SELECT * FROM list') # все поля из list
    list = cur.fetchall()

    info = ''
    for el in list:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n' # 0 елемент - id int auto_incerment primary key (айди текущей записи) 1 - имя, 2 - пароль
    
    #conn.commit() - нужна для установки, обновление, удаление (тут получаем данные) -> cur.fetchall()
    cur.close ()
    conn.close()

    bot.send_message(call.message.chat.id, info) # сначало call, потому что обращаемся сначало к функции

bot.polling(none_stop=True)