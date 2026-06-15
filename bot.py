import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

import handlers.start as start_module
import handlers.playbook as playbook_module


async def main():

    if not BOT_TOKEN:
        print("BOT_TOKEN missing")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_module.router)
    dp.include_router(playbook_module.router)

    print("Bot running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
