import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.playbook import router as playbook_router


async def main():

    # Check token safely
    if not BOT_TOKEN:
        print("BOT_TOKEN missing")
        return

    try:
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        # Register handlers
        dp.include_router(start_router)
        dp.include_router(playbook_router)

        print("BitClaw AI Bot Started")

        await dp.start_polling(bot)

    except Exception:
        # Silent fail (no crash spam)
        print("Bot failed to start")


if __name__ == "__main__":
    asyncio.run(main())
