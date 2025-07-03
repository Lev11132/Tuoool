import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_gpt(prompt):
    try:
        completion = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",
            messages=[{"role": "user", "content": prompt}],
            extra_headers={
                "HTTP-Referer": "https://your-site.com",
                "X-Title": "JarvisMistral"
            },
            extra_body={}
        )
        return completion.choices[0].message.content
    except Exception as e:
        print("❌ GPT Error:", e)
        return "⚠️ Виникла помилка при зверненні до моделі."
