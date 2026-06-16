from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def playbook_handler(message: Message):
    await message.answer("✅ Message received")
