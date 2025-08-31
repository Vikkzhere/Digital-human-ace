from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, io, numpy as np, soundfile as sf
from dotenv import load_dotenv

from services.asr import asr_transcribe
from services.llm import llm_chat
from services.tts import tts_synthesize
from services.a2f import audio_to_visemes

load_dotenv()
MODE = os.getenv("MODE","MOCK").upper()

app = FastAPI(title="Digital Human ACE-Inspired API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status":"ok","mode":MODE}

@app.post("/api/stt")
async def stt(file: UploadFile):
    # Accept a short WAV/PCM audio and return text
    audio_bytes = await file.read()
    text = asr_transcribe(audio_bytes)
    return {"text": text}

@app.post("/api/chat")
async def chat(payload: ChatIn):
    reply = llm_chat(payload.text)
    return {"reply": reply}

@app.post("/api/tts")
async def tts(payload: ChatIn):
    # Returns WAV bytes (base64) and visemes array [{t, v}] in MOCK mode
    wav_bytes = tts_synthesize(payload.text)
    visemes = audio_to_visemes(wav_bytes)
    import base64
    b64 = base64.b64encode(wav_bytes).decode("ascii")
    return {"audio_wav_b64": b64, "visemes": visemes}
