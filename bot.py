import asyncio
import os
import threading

from fastapi import FastAPI
import uvicorn

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from start import router as start_router
from risk import router as risk_router
from review import router as review_router
from playbook import router as playbook_router


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "BitClaw AI Running"}


async def run_bot():

    if not BOT_TOKEN:
        print("BOT_TOKEN missing")
        return

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(risk_router)
    dp.include_router(review_router)
    dp.include_router(playbook_router)

    print("🦾 BitClaw AI running...")

    await dp.start_polling(bot)


def start_web():

    port = int(os.getenv("PORT", 10000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )


if __name__ == "__main__":

    threading.Thread(
        target=start_web, daemon=True
    ).start()

    asyncio.run(run_bot())
