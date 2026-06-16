from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.startswith("/risk"))
async def risk_command(message: Message):
    await message.answer(
        "🛡 Risk Manager\n\nUsage:\n/risk 1000 2\n\nExample:\n/risk 1000 2"
    )
