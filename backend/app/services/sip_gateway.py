"""SIP gateway adapter (stubbed for development)."""
from typing import Dict, Any

_TRUNKS = {}

def register_trunk(trunk: Dict[str, Any]) -> bool:
    name = trunk.get("name")
    if not name:
        return False
    _TRUNKS[name] = trunk
    return True

def get_trunk(name: str):
    return _TRUNKS.get(name)

def simulate_incoming_audio(call_id: str, frames: bytes):
    return True
