from aiogram import Router
from aiogram.types import CallbackQuery, Message

from services.gemini import generate_text

router = Router()

# button click
@router.callback_query(lambda c: c.data == "playbook")
async def playbook_button(call: CallbackQuery):
    await call.message.answer("Send your trading style (example: breakout, scalping)")

    await call.answer()


# ONLY SAFE VERSION (no conflict)
@router.message()
async def handle_text(message: Message):

    if not message.text:
        return

    prompt = f"""
You are a crypto trading expert.

User style: {message.text}

Create structured playbook:
- Strategy name
- Entry rules
- Exit rules
- Risk management
"""

    result = await generate_text(prompt)

    await message.answer(result)
