import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '5927005651:AAEz73wVkuUEsd23qZNJrV773BFf4dUihx4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

all_answers = []

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'correct_option': 'Paris'
    },
    {
        'question': 'How many continents are there?',
        'options': ['5', '6', '7', '8'],
        'correct_option': '5'
    },

]


user_data = {}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardRemove()
    await message.answer("Привет! Давай начнем тест. Нажми /test, чтобы начать.", reply_markup=markup)
    user_data[message.from_user.id] = {'score': 0, 'current_question': 0}


@dp.message_handler(commands=['test'])
async def start_test(message: types.Message):
    if message.from_user.id in user_data:
        user_data[message.from_user.id]['score'] = 0
        user_data[message.from_user.id]['current_question'] = 0
    else:
        user_data[message.from_user.id] = {'score': 0, 'current_question': 0}

    await ask_question(message.from_user.id, message)


@dp.callback_query_handler(lambda c: c.data.startswith('answer_'))
async def process_callback_answer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    chosen_answer = callback_query.data.split('_')[1]
    current_question = user_data[user_id]['current_question']
    question_data = questions[current_question]
    correct_answer = question_data['correct_option']

    all_answers.append({
        'question': question_data['question'],
        'chosen_answer': chosen_answer,
        'correct_answer': correct_answer
    })

    if chosen_answer == correct_answer:
        user_data[user_id]['score'] += 1

    user_data[user_id]['current_question'] += 1

    if user_data[user_id]['current_question'] < len(questions):
        await ask_question(user_id, callback_query.message)
    else:
        await show_test_results(user_id, callback_query.message)


async def show_test_results(user_id, message):
    score = user_data[user_id]['score']
    result_message = f'Тест завершен! Твой результат: {score}/{len(questions)}\n\n'

    for i, answer_data in enumerate(all_answers):
        result_message += f'Вопрос {i + 1}: {answer_data["question"]}\n'
        result_message += f'Твой ответ: {answer_data["chosen_answer"]}\n'
        result_message += f'Правильный ответ: {answer_data["correct_answer"]}\n\n'

    await message.answer(result_message)




async def ask_question(user_id, message):
    current_question = user_data[user_id]['current_question']

    if current_question < len(questions):
        question_data = questions[current_question]
        options = question_data['options']

        random.shuffle(options)

        markup = InlineKeyboardMarkup()
        for option in options:
            markup.add(InlineKeyboardButton(option, callback_data=f'answer_{option}'))

        await message.answer(question_data['question'], reply_markup=markup)
    else:
        score = user_data[user_id]['score']
        await message.answer(f'Тест завершен! Твой результат: {score}/{len(questions)}')



if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
