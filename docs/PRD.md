# Product Requirements Document (PRD)

## Introduction
This PRD describes the call-agent (robocall) and IVR broadcast MVP for WhatsApp and PSTN/GSM channels.

## MVP Engines
- Call agent inbound
- Call agent outbound
- IVR broadcast outbound (one-way, non-keypad)

## Objectives
1. Increase Call Center efficiency (faster response, reduced agent load)
2. Provide 24/7 services to end-users

## Key Requirements (20 total)
1. Latency: 3-4 seconds max response time
2. Model selection: benchmark by accuracy, tone, price, compliance
3. User-made prompts: flexible custom prompts
4. Keyword/topic detection: auto-switching on out-of-topic
5. Call transfer: attended transfer to human agents
6. Call termination: auto-hangup with closing statement
7. IVR broadcast: one-way audio, no interaction
8. Multilingual: Indonesian & English auto-detection
9. Cultural intelligence: dialect, slang, accent support
10. Document processing: knowledge source from docs
11. Placeholder replacement: CSV {column_name} substitution
12. SIP trunk integration: direct SIP trunk connection
13. Number deployment: easy deploy/switch on numbers
14. Concurrent calls: 100 default concurrency
15. Recording: audio storage (3 months max)
16. Real-time transcript: live text conversion
17. Summary: call summary extraction
18. Sentiment analysis: real-time emotion detection
19. Conversational memory: context retention per call
20. VAD: robust Voice Activity Detection

## Non-Functional Requirements
- Performance: 3-4s max latency
- Scalability: handle growing user/call volumes
- Reliability: 99.9% uptime minimum
- Security: encryption, privacy protection

See the full PRD in the original document for complete details.
