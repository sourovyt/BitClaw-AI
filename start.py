from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(lambda message: message.text == "/start")
async def start_command(message: Message):

    kb = InlineKeyboardBuilder()

    kb.button(text="🚀 AI Playbook", callback_data="playbook")
    kb.button(text="🛡 Risk Manager", callback_data="risk")
    kb.button(text="📊 Trade Review", callback_data="review")
    kb.button(text="📈 Chart Analysis", callback_data="chart")

    kb.adjust(1)

    await message.answer(
        """
🦾 Welcome to BitClaw AI

Your AI-Powered Crypto Trading Assistant

Available Tools:

🚀 AI Playbook Generator
🛡 Risk Manager
📊 Trade Review
📈 Chart Analysis

Select a tool below:
""",
        reply_markup=kb.as_markup()
    )


@router.callback_query(lambda c: c.data == "playbook")
async def playbook_callback(callback: CallbackQuery):

    await callback.message.answer(
        "🚀 Send your trading strategy.\n\nExample:\nscalping ETH on 5m timeframe"
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "risk")
async def risk_callback(callback: CallbackQuery):

    await callback.message.answer(
        "🛡 Risk Manager\n\nUsage:\n/risk 1000 2\n\nExample:\n/risk 1000 2"
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "review")
async def review_callback(callback: CallbackQuery):

    await callback.message.answer(
        "📊 Trade Review\n\nUsage:\n/review\n\nEntry: 108000\nExit: 109500\nSL: 107500\nReason: ETH breakout"
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "chart")
async def chart_callback(callback: CallbackQuery):

    await callback.message.answer(
        "📈 Chart Analysis\n\nSend market details.\n\nExample:\nBTC 1H\nPrice above EMA200\nRSI 68\nResistance 108000"
    )

    await callback.answer()
