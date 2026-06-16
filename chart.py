from aiogram import Router, F
from aiogram.types import Message

from gemini import generate_text

router = Router()


@router.message(F.text.startswith("/chart"))
async def chart_command(message: Message):

    chart_text = message.text.replace("/chart", "").strip()

    if not chart_text:
        await message.answer(
            "📈 Usage:\n\n/chart\nBTC 1H\nPrice above EMA200\nRSI 68\nResistance 108000"
        )
        return

    loading = await message.answer(
        "📈 BitClaw AI is analyzing the chart..."
    )

    prompt = f"""
Analyze this crypto chart information:

{chart_text}

Provide:

📈 Trend
🎯 Support Levels
🚧 Resistance Levels
⚠ Risks
🚀 Potential Trade Setup

Keep it concise.
"""

    try:
        response = await generate_text(prompt)
        await loading.edit_text(response[:3900])

    except Exception as e:
        await loading.edit_text(f"❌ Error: {e}")
