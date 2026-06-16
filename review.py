from aiogram import Router, F
from aiogram.types import Message

from gemini import generate_text

router = Router()


@router.message(F.text.startswith("/review"))
async def review_command(message: Message):

    trade_text = message.text.replace("/review", "").strip()

    if not trade_text:
        await message.answer(
            "📊 Trade Review\n\nExample:\n\n/review\nEntry: 108000\nExit: 109500\nSL: 107500\nReason: ETH breakout"
        )
        return

    loading = await message.answer(
        "📊 BitClaw AI is reviewing your trade..."
    )

    prompt = f"""
You are a professional crypto trading mentor.

Review this trade:

{trade_text}

Provide:

📊 Trade Review

✅ Strengths

⚠ Weaknesses

🎯 Improvements

⭐ Score out of 10

Keep the response concise and under 2000 characters.
"""

    try:
        response = await generate_text(prompt)

        if len(response) > 3900:
            response = response[:3900]

        await loading.edit_text(response)

    except Exception as e:
        await loading.edit_text(
            f"❌ Review failed: {str(e)}"
        )
