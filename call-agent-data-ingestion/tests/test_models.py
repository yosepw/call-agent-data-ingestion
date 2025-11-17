import pytest
from main import IngestionPayload
from datetime import datetime


def test_valid_payload_parses():
    payload = {
        "user_id": "user_123",
        "timestamp": "2025-01-01T12:00:00Z",
        "data_payload": {"key": "value"},
    }
    obj = IngestionPayload.parse_obj(payload)
    assert obj.user_id == "user_123"
    assert isinstance(obj.timestamp, datetime)
    assert obj.data_payload["key"] == "value"


def test_invalid_timestamp_raises():
    payload = {
        "user_id": "user_123",
        "timestamp": "not-a-datetime",
        "data_payload": {},
    }
    with pytest.raises(Exception):
        IngestionPayload.parse_obj(payload)
