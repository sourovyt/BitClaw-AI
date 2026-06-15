import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "🦾 Welcome to BitClaw AI\n\n"
        "Your AI-Powered Crypto Trading Agent"
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
