from aiogram import Router, F
from aiogram.types import Message

from gemini import analyze_chart

router = Router()


@router.message(F.photo)
async def chart_analysis(message: Message):

    loading = await message.answer(
        "📈 BitClaw AI is analyzing your chart..."
    )

    try:

        photo = message.photo[-1]

        file = await message.bot.get_file(photo.file_id)

        image_path = "chart.jpg"

        await message.bot.download_file(
            file.file_path,
            destination=image_path
        )

        result = await analyze_chart(image_path)

        if len(result) > 3900:
            result = result[:3900]

        await loading.edit_text(result)

    except Exception as e:

        await loading.edit_text(
            f"❌ Chart analysis failed:\n{str(e)}"
        )
