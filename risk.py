from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.startswith("/risk"))
async def risk_command(message: Message):
    try:
        parts = message.text.split()

        if len(parts) != 3:
            await message.answer(
                "🛡 Risk Manager\n\nUsage:\n/risk 1000 2\n\nExample:\n/risk 1000 2"
            )
            return

        account_size = float(parts[1])
        risk_percent = float(parts[2])

        max_risk = account_size * (risk_percent / 100)

        reply = f"""
🛡 Risk Report

💰 Account Size: ${account_size:,.2f}
📊 Risk Per Trade: {risk_percent}%

⚠ Maximum Loss:
${max_risk:,.2f}

📋 Risk Rules
• Always use a stop loss
• Maintain at least 1:2 Risk/Reward
• Never exceed your risk limit
• Avoid revenge trading

🚀 Trade Smart. Protect Capital First.
"""

        await message.answer(reply)

    except Exception:
        await message.answer(
            "❌ Invalid format.\n\nExample:\n/risk 1000 2"
        )
