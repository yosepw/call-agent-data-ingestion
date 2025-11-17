# Call Agent Data Ingestion  Project Overview & PRD Summary

This repository implements the backend and supporting components for a call-agent (robocall/IVR) MVP.

## MVP Capabilities
- Call agent inbound (conversational voice agent)
- Call agent outbound (agent-driven calls)
- IVR broadcast outbound (one-way, non-interactive)

## Key Requirements
- Latency target: time-to-first-word <= 3-4s (ideal < 2.5s)
- Concurrency: 100 concurrent calls default
- Retention: 3 months for recordings, transcripts, summaries
- Languages: Indonesian and English with auto-detection
- Features: VAD, ASR, LLM, TTS, SIP trunk integration, transfer, real-time transcript

## Quick Start (Local Dev)

\\\powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
\\\

Open \http://127.0.0.1:8000/\ in your browser.

## Docker Compose

\\\powershell
docker-compose up --build
\\\

## Run Tests

\\\powershell
pytest -q
\\\

## Architecture

1. Client audio via PSTN/SIP -> SIP/RTC Gateway
2. Gateway runs VAD, buffers audio
3. Audio -> STT service (ASR) returns transcript
4. Transcript -> Ngobrol LLM generates response
5. Response -> TTS service produces audio (base64)
6. Audio -> Gateway -> Client

## Next Steps

- Integrate real ASR/TTS/LLM endpoints (replace stubs)
- Implement Celery/RQ workers for concurrent blasts
- Add CI/CD workflow
- Wire SIP trunk simulation for load testing

See \.github/copilot-instructions.md\ for developer guidance.
