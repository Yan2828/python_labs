import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

# Ваш токен бота
BOT_TOKEN = "8491914338:AAEivzx8CzgFbbfiqfir_hbVaX9ngXEj95A"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = """
🤖 **Добро пожаловать в AlfaBiz Assistant!**

Я ваш ИИ-помощник для малого бизнеса. Я могу помочь с:

📊 **Финансы** - анализ расходов, финансовые советы
⚖️ **Юридические вопросы** - договоры, правовые консультации
📱 **Маркетинг** - контент для соцсетей, промоакции
📝 **Документы** - генерация и редактирование документов
💼 **Операционные задачи** - чек-листы, процессы

Выберите категорию помощи из меню ниже!
    """
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="💼 Финансы"), types.KeyboardButton(text="⚖️ Юридические вопросы")],
            [types.KeyboardButton(text="📱 Маркетинг"), types.KeyboardButton(text="📝 Документы")],
            [types.KeyboardButton(text="🔧 Операционные задачи")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="Markdown")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = """
📖 **Доступные команды:**

/start - Главное меню
/help - Эта справка
/finance - Финансовые вопросы
/legal - Юридические консультации
/marketing - Помощь с маркетингом

💡 **Используйте кнопки меню** для быстрого доступа к функциям!
    """
    await message.answer(help_text)

# Обработчики для кнопок
@router.message(lambda message: message.text == "💼 Финансы")
async def finance_help(message: types.Message):
    response = """
💼 **Финансовая помощь:**

• Анализ расходов и доходов
• Налоговое планирование  
• Финансовые отчеты
• Бюджетирование и прогнозирование
• Оптимизация затрат

Опишите вашу финансовую задачу, и я помогу её решить!
"""
    await message.answer(response)

@router.message(lambda message: message.text == "⚖️ Юридические вопросы")
async def legal_help(message: types.Message):
    response = """
⚖️ **Юридические консультации:**

• Составление договоров
• Регистрация бизнеса
• Трудовые вопросы
• Правовые консультации
• Помощь с документацией

Задайте ваш юридический вопрос!
"""
    await message.answer(response)

@router.message(lambda message: message.text == "📱 Маркетинг")
async def marketing_help(message: types.Message):
    response = """
📱 **Маркетинговая помощь:**

• Контент для соцсетей
• Промоакции и скидки
• Анализ аудитории
• Рекламные тексты
• Стратегии продвижения

Что вас интересует в маркетинге?
"""
    await message.answer(response)

@router.message(lambda message: message.text == "📝 Документы")
async def documents_help(message: types.Message):
    response = """
📝 **Помощь с документами:**

• Шаблоны договоров
• Деловые письма
• Коммерческие предложения
• Отчеты и формы
• Редактирование документов

Какой документ вам нужен?
"""
    await message.answer(response)

@router.message(lambda message: message.text == "🔧 Операционные задачи")
async def operations_help(message: types.Message):
    response = """
🔧 **Операционные задачи:**

• Чек-листы процессов
• Оптимизация workflows
• Управление задачами
• Ежедневные операции
• Автоматизация рутины

С какой операционной задачей помочь?
"""
    await message.answer(response)

# Команды
@router.message(Command("finance"))
async def finance_command(message: types.Message):
    await finance_help(message)

@router.message(Command("legal"))
async def legal_command(message: types.Message):
    await legal_help(message)

@router.message(Command("marketing"))
async def marketing_command(message: types.Message):
    await marketing_help(message)

# Обработка любых других сообщений
@router.message()
async def echo(message: types.Message):
    response = f"""
🤖 Я получил ваше сообщение: "{message.text}"

Используйте меню для выбора категории помощи или команды:
/start - главное меню
/help - справка по командам
"""
    await message.answer(response)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("🤖 Бот запускается...")
    
    dp.include_router(router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    print("✅ Бот успешно запущен!")
    print("📱 Теперь перейдите в Telegram и напишите /start вашему боту")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())