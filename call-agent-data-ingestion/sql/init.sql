-- SQL script to create ingestion_log table
CREATE TABLE IF NOT EXISTS ingestion_log (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    data_payload JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
