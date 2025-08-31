# Digital Human (NVIDIA ACE-inspired)

Prototype **AI digital human** with a FastAPI backend and a lightweight web avatar. Runs locally in **MOCK mode** (no GPU needed) and can be switched to **REAL mode** with NVIDIA services (Riva ASR/TTS, Nemotron via NIM, Audio2Face).

## ✨ What it does
- 🎙️ Speech → Riva ASR (or mock text)
- 🧠 Intelligence → Nemotron (NIM) (or mock replies)
- 😀 Lip-sync → Audio2Face visemes (or mock visemes)
- ⚡ Realtime demo → FastAPI + HTML/JS avatar

## 🚀 Quickstart (MOCK mode)
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload --port 8000
python -m http.server 5173 -d frontend   # open http://localhost:5173
