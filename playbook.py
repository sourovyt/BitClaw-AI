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

Create a concise professional trading playbook for:

{message.text}

Format:

🚀 Strategy Name

🎯 Entry Rules
- Rule 1
- Rule 2

💰 Exit Rules
- Rule 1
- Rule 2

🛡 Risk Management
- Risk rule 1
- Risk rule 2

⚠ Common Mistakes
- Mistake 1
- Mistake 2

Keep the response under 3000 characters.
"""

        response = await generate_text(prompt)

        if len(response) > 3900:
            response = response[:3900] + "\n\n...truncated"

        await loading.edit_text(response)

    except Exception as e:
        await message.answer(f"❌ Error: {str(e)}")
