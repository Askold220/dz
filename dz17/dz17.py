import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    )
''')
conn.commit()

API_TOKEN = '5927005651:AAEz73wVkuUEsd23qZNJrV773BFf4dUihx4'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def find_user(user_id=None, username=None):
    query = 'SELECT * FROM users WHERE '
    params = []

    if user_id:
        query += 'telegram_id = ?'
        params.append(user_id)
    elif username:
        query += 'username LIKE ?'
        params.append(f'%{username}%')

    cursor.execute(query, params)
    return cursor.fetchall()

def add_user(telegram_id, username, first_name, last_name):
    cursor.execute('''
        INSERT INTO users (telegram_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (telegram_id, username, first_name, last_name))
    conn.commit()

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE telegram_id = ?', (user_id,))
    conn.commit()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привіт! Я твій телеграм-бот для роботи з базою даних користувачів.")

@dp.message_handler(commands=['search'])
async def search_user(message: types.Message):
    await message.answer("Введіть ID або ім'я користувача, якого ви шукаєте.")

@dp.message_handler(lambda message: message.text.isdigit() or message.text.startswith('@'))
async def handle_search_input(message: types.Message):
    user_id = None
    username = None

    if message.text.isdigit():
        user_id = int(message.text)
    else:
        username = message.text[1:]

    result = find_user(user_id, username)

    if result:
        await message.answer(f"Результат пошуку:\n{result}")
    else:
        await message.answer("Користувача не знайдено.")

@dp.message_handler(commands=['add'])
async def add_user_command(message: types.Message):
    await message.answer("Введіть дані нового користувача у форматі: ID, Ім'я, Прізвище, Логін.")

@dp.message_handler(lambda message: message.text.count(',') == 3)
async def handle_add_input(message: types.Message):
    try:
        user_data = message.text.split(',')
        telegram_id = int(user_data[0])
        username = user_data[3].strip()
        first_name = user_data[1].strip()
        last_name = user_data[2].strip()

        add_user(telegram_id, username, first_name, last_name)
        await message.answer("Користувача додано до бази даних.")
    except Exception as e:
        await message.answer(f"Помилка при додаванні користувача: {e}")

@dp.message_handler(commands=['delete'])
async def delete_user_command(message: types.Message):
    await message.answer("Введіть ID користувача, якого ви хочете видалити.")

@dp.message_handler(lambda message: message.text.isdigit())
async def handle_delete_input(message: types.Message):
    try:
        user_id = int(message.text)
        delete_user(user_id)
        await message.answer("Користувача видалено з бази даних.")
    except Exception as e:
        await message.answer(f"Помилка при видаленні користувача: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
