from aiogram import Router
from aiogram.types import Message
from gemini import generate_text

router = Router()

@router.message()
async def playbook_handler(message: Message):
    try:
        response = await generate_text(message.text)
        await message.answer(response)
    except Exception as e:
        await message.answer(f"ERROR: {str(e)}")
