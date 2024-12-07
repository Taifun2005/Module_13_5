from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')

kb.insert(button1)
kb.insert(button2)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью введите "Рассчитать" чтобы посчитать вашу норму колорий', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    # data_age = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    # data_growth = await state.get_data()
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    # norma_call = (10 х UserState.weight) + (6,25 х UserState.weight) – (5 х UserState.growth) + 5.
    norma_call = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) + 5
    await message.answer(f'Ваша норма колорий {norma_call}')
    # Для мужчин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5.
    await state.finish()


@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью введите "Рассчитать" чтобы посчитать вашу норму колорий')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContextfrom
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начало')

kb.add(button1)
kb.add(button2)
# kb.row (в один ряд) kb.insert (добавляет в конец ряда)


@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет!', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Информация о боте')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
"""
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью введите "Calories" чтобы посчитать вашу норму колорий')


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    # data_age = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    # data_growth = await state.get_data()
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    # norma_call = (10 х UserState.weight) + (6,25 х UserState.weight) – (5 х UserState.growth) + 5.
    norma_call = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) + 5
    await message.answer(f'Ваша норма колорий {norma_call}')
    # Для мужчин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5.
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
"""
"""

@dp.message_handler(text='Заказать')
async def buy(message: types.Message):
    await message.answer('Отправь нам свой адрес, пожалуйста.')
    await UserState.adres.set()


@dp.message_handler(state = UserState.adres)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()





from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')


# @dp.message_handler(text=['Urban', 'ff'])
# async def urban_message(message):
#     print('Urban message')
#     await message.answer('Urban message')


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""

"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7890890424:AAEwL3AvXADeymJq1hsVzEH_kAkWYnGdBsc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer('Рады вас видеть')

@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')
    await message.answer('Urban message')


@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
"""
