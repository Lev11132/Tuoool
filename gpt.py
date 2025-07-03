import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_gpt(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        r.raise_for_status()
        json = r.json()
        print("✅ GPT JSON Response:", json)
        return json["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ GPT API error:", r.status_code, r.text)
        return "⚠️ GPT не відповів. Можливо, проблема з API або лімітом."
