"""ASR (STT) adapter stub."""
from typing import Dict, Any

def transcribe_audio_bytes(audio_bytes: bytes, language: str = "id") -> Dict[str, Any]:
    return {"text": "halo, saya butuh bantuan", "language": language, "confidence": 0.95}
