from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "🦾 Welcome to BitClaw AI\n\n"
        "Send your trading strategy and I'll generate an AI trading playbook."
    )
