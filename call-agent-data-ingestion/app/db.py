import os
import json
from typing import Optional


class PostgreSQLConnector:
    """
    Minimal async PostgreSQL connector using asyncpg.
    """

    def __init__(self):
        self.pool = None

    async def connect(self):
        import asyncpg
        host = os.getenv("DB_HOST")
        port = int(os.getenv("DB_PORT", "5432"))
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")
        if not all([host, user, password, database]):
            raise RuntimeError("Database credentials are not fully configured in environment variables")
        self.pool = await asyncpg.create_pool(
            host=host, port=port, user=user, password=password, database=database, min_size=1, max_size=5
        )

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def insert_record(self, user_id: str, timestamp, data_payload) -> int:
        if not self.pool:
            raise RuntimeError("Database connection pool is not initialized")
        async with self.pool.acquire() as conn:
            query = """
            INSERT INTO ingestion_log (user_id, timestamp, data_payload)
            VALUES ($1, $2, $3::jsonb)
            RETURNING id
            """
            rec_id = await conn.fetchval(query, user_id, timestamp, json.dumps(data_payload))
            return rec_id
