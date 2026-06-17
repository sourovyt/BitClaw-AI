from google import genai
from PIL import Image

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


async def generate_text(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


async def analyze_chart(image_path):

    image = Image.open(image_path)

    prompt = """
You are a professional crypto technical analyst.

Analyze this trading chart screenshot.

Return ONLY in this format:

📈 Trend
• point

🎯 Support
• point

🚧 Resistance
• point

⚠ Risks
• point

🚀 Trade Setup
• point

Rules:
- Keep under 1200 characters
- Use bullet points
- No long paragraphs
- Give realistic support and resistance levels visible on chart
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    return response.text
