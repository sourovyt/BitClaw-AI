import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from start import router as start_router
from playbook import router as playbook_router


async def main():

    if not BOT_TOKEN:
        print("BOT_TOKEN missing")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(playbook_router)

    print("BitClaw AI running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
