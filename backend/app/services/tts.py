"""TTS adapter stub."""
import base64
from typing import Dict

def synthesize_text(text: str, voice: str = "default") -> Dict[str, str]:
    placeholder = b"\x00\x00\x00\x00"
    return {"audio_base64": base64.b64encode(placeholder).decode("ascii"), "voice": voice}
