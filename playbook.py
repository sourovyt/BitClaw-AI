from aiogram import Router
from aiogram.types import Message

from gemini import generate_text

router = Router()


@router.message()
async def playbook_handler(message: Message):

    prompt = f"""
Create a professional crypto trading playbook.

User strategy:
{message.text}

Include:
1. Strategy Name
2. Entry Rules
3. Exit Rules
4. Risk Management
5. Common Mistakes
"""

    response = await generate_text(prompt)

    await message.answer(response)
