from aiogram import Router, F
from aiogram.types import Message

from gemini import generate_text

router = Router()


@router.message(F.text.startswith("/review"))
async def review_trade(message: Message):

    trade_text = message.text.replace("/review", "").strip()

    if not trade_text:
        await message.answer(
            "📊 Usage:\n\n/review Entry: 108000 Exit: 109500 SL: 107500"
        )
        return

    loading = await message.answer(
        "📊 BitClaw AI is reviewing your trade..."
    )

    prompt = f"""
You are a professional crypto trading mentor.

Review this trade:

{trade_text}

Format:

📊 Trade Review

✅ Strengths
• point

⚠ Weaknesses
• point

🎯 Improvements
• point

⭐ Score
X/10

Keep under 1000 characters.
"""

    try:
        result = await generate_text(prompt)

        if len(result) > 3900:
            result = result[:3900]

        await loading.edit_text(result)

    except Exception as e:
        await loading.edit_text(
            f"❌ Error: {str(e)}"
        )
