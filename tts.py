import asyncio
import edge_tts

async def text_to_voice(text, file_path):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    await communicate.save(file_path)
