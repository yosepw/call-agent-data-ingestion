## Purpose
Guidance for AI agents working on the call-agent-data-ingestion repo.

## Big Picture
- **End-to-end flow**: SIP/RTC Gateway <-> VAD -> STT -> Ngobrol LLM -> TTS
- **MVP features**: inbound calls, outbound calls, IVR broadcast, transfer, transcripts

## Key Constraints
- **Latency**: <= 3-4s time-to-first-word (ideal <2.5s)
- **Concurrency**: 100 default for blasts
- **Retention**: 3 months for recordings/transcripts
- **Languages**: Indonesian and English with auto-detection

## Project Structure
- \ackend/app/main.py\ - FastAPI entrypoint
- \ackend/app/api/*.py\ - REST endpoints
- \ackend/app/services/*.py\ - ASR, TTS, LLM stubs
- \rontend/\ - Minimal static UI
- \	ests/\ - Pytest suite
- \docs/PRD.md\ - Full PRD

## Developer Workflows
\\\
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
pytest -q
\\\

## Integration Points
- ASR/TTS/LLM: service stubs ready for real endpoints
- SIP Trunk: onboarding form with validation
- Helpdesk: webhook for call transfers
