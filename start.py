from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Playbook"),
            KeyboardButton(text="🛡 Risk")
        ],
        [
            KeyboardButton(text="📊 Review"),
            KeyboardButton(text="📈 Chart")
        ],
        [
            KeyboardButton(text="ℹ️ Help")
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)


@router.message(lambda message: message.text == "/start")
async def start_command(message: Message):

    await message.answer(
        """
🦾 Welcome to BitClaw AI

Your AI-Powered Crypto Trading Assistant

Available Tools:

🚀 Playbook Generator
🛡 Risk Manager
📊 Trade Review
📈 Chart Analysis

Select a tool below.
""",
        reply_markup=menu
    )


@router.message(lambda message: message.text == "🚀 Playbook")
async def playbook_help(message: Message):
    await message.answer(
        "🚀 Send any trading strategy.\n\nExample:\nscalping ETH on 5m timeframe"
    )


@router.message(lambda message: message.text == "🛡 Risk")
async def risk_help(message: Message):
    await message.answer(
        "🛡 Usage:\n/risk 1000 2\n\nExample:\n/risk 1000 2"
    )


@router.message(lambda message: message.text == "📊 Review")
async def review_help(message: Message):
    await message.answer(
        "📊 Usage:\n/review\n\nEntry: 108000\nExit: 109500\nSL: 107500\nReason: ETH breakout"
    )


@router.message(lambda message: message.text == "📈 Chart")
async def chart_help(message: Message):
    await message.answer(
        "📈 Usage:\n/chart\nBTC 1H\nPrice above EMA200\nRSI 68\nResistance 108000"
    )


@router.message(lambda message: message.text == "ℹ️ Help")
async def help_command(message: Message):
    await message.answer(
        """
🦾 BitClaw AI Commands

🚀 Playbook
Generate AI trading strategies

🛡 Risk
Calculate risk per trade

📊 Review
Review completed trades

📈 Chart
Analyze chart setups
"""
    )
