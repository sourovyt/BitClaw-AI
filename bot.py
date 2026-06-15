import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# handlers
from handlers.start import router as start_router
from handlers.playbook import router as playbook_router


dp = Dispatcher()

# register routers
dp.include_router(start_router)
dp.include_router(playbook_router)


async def main():
    bot = Bot(token=BOT_TOKEN)

    print("🦾 BitClaw AI Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
