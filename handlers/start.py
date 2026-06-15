from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message):

    kb = InlineKeyboardBuilder()

    kb.button(text="📸 Analyze Chart", callback_data="chart")
    kb.button(text="📊 Market Scan", callback_data="scan")

    kb.button(text="⚡ AI Playbook", callback_data="playbook")
    kb.button(text="🛡 Risk Manager", callback_data="risk")

    kb.button(text="🔍 Trade Review", callback_data="review")
    kb.button(text="📰 Market Intel", callback_data="intel")

    kb.adjust(2)

    await message.answer(
        "🦾 Welcome to BitClaw AI\n\n"
        "Your AI-Powered Crypto Trading Agent",
        reply_markup=kb.as_markup()
    )
