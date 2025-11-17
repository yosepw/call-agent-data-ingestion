import pytest
import asyncio
from app.db import PostgreSQLConnector


class DummyConn:
    async def fetchval(self, query, *args):
        return 42


class DummyAcquire:
    async def __aenter__(self):
        return DummyConn()

    async def __aexit__(self, exc_type, exc, tb):
        return False


class DummyPool:
    async def acquire(self):
        return DummyAcquire()


@pytest.mark.asyncio
async def test_insert_record_monkeypatched(monkeypatch):
    async def fake_create_pool(**kwargs):
        return DummyPool()

    monkeypatch.setattr("asyncpg.create_pool", fake_create_pool)

    connector = PostgreSQLConnector()
    await connector.connect()
    rec_id = await connector.insert_record("u1", "2025-01-01T00:00:00Z", {"a": 1})
    assert rec_id == 42
    await connector.close()
