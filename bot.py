import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "#"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

users = {}

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Hello, {name}! Я твой учебный бот.")

@dp.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer(
        "Я умею:\n"
        "/start\n"
        "/help\n"
        "/stat\n"
        "привет\n"
        "спасибо\n"
        "кто ты"
    )
@dp.message(Command(commands=["stat"]))
async def cmd_stat(message: Message):
    user_id = message.from_user.id
    users[user_id] = users.get(user_id, 0)
    await message.answer(f"Ты написал: {users[user_id]} сообщений")

@dp.message(F.text.lower() == "привет")
async def cmd_hello(message: Message):
    await message.answer("Привет!")

@dp.message(F.text().lower() == "спасибо")
async def cmd_thanks(message: Message):
    await message.answer("Пожалуйста")

@dp.message(F.text.lower() == "кто ты")
async def cmd_how(message: Message):
    await message.answer("Я учебный бот.")

@dp.message()
async def cmd_echo(message: Message):
    user_id = message.from_user.id
    name =  message.from_user.first_name
    users[user_id] = users.get(user_id, 0) + 1
    await message.answer(f"{name}, ты написал {users[user_id]} сообщений")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())