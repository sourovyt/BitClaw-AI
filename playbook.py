from aiogram import Router
from aiogram.types import Message

from gemini import generate_text

router = Router()


@router.message()
async def playbook_handler(message: Message):
    try:

        loading = await message.answer(
            "🦾 BitClaw AI is analyzing your strategy..."
        )

        prompt = f"""
You are an expert crypto trading strategist.

Create a professional crypto trading playbook for:

{message.text}

Format:

🚀 Strategy Name

🎯 Entry Rules
- Bullet points

💰 Exit Rules
- Bullet points

🛡 Risk Management
- Bullet points

⚠ Common Mistakes
- Bullet points

📈 Market Conditions
- When this strategy works best

Keep the response concise and under 2500 characters.
"""

        response = await generate_text(prompt)

        if len(response) > 3900:
            response = response[:3900] + "\n\n...truncated"

        await loading.edit_text(response)

    except Exception as e:
        await message.answer(
            f"❌ Error: {str(e)}"
        )
