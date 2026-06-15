from aiogram import Router
from aiogram.types import CallbackQuery, Message

from services.gemini import generate_text

router = Router()


@router.callback_query(lambda c: c.data == "playbook")
async def playbook_button(call: CallbackQuery):
    await call.message.answer("⚡ Send your trading style (example: breakout, scalping, swing)")



@router.message()
async def handle_playbook(message: Message):

    text = message.text

    prompt = f"""
You are a professional crypto trading strategist.

User trading style: {text}

Generate a structured trading playbook:

1. Strategy name
2. Entry rules
3. Exit rules
4. Risk management
5. Best market condition
"""

    result = await generate_text(prompt)

    await message.answer(f"⚡ AI Playbook:\n\n{result}")
