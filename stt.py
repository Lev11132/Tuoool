from faster_whisper import WhisperModel

model = WhisperModel("base")

def voice_to_text(path):
    segments, _ = model.transcribe(path)
    return " ".join([seg.text for seg in segments])
