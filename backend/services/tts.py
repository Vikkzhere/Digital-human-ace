import os, io, numpy as np, soundfile as sf

def tts_synthesize(text: str) -> bytes:
    mode = os.getenv("MODE","MOCK").upper()
    if mode == "REAL":
        # TODO: implement Riva TTS client.
        # Return raw WAV bytes.
        return b""
    # MOCK: generate a 0.8-second sine "beep" so browsers can play something
    sr = 16000
    dur = 0.8
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    y = 0.05*np.sin(2*np.pi*440*t).astype(np.float32)
    buf = io.BytesIO()
    sf.write(buf, y, sr, format="WAV")
    return buf.getvalue()
