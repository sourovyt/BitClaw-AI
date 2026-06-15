from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):

    kb = InlineKeyboardBuilder()

    kb.button(text="⚡ AI Playbook", callback_data="playbook")

    kb.adjust(1)

    await message.answer(
        "🦾 BitClaw AI Ready\n\nChoose an option:",
        reply_markup=kb.as_markup()
    )
