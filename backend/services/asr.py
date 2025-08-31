import os
def asr_transcribe(audio_bytes: bytes) -> str:
    mode = os.getenv("MODE","MOCK").upper()
    if mode == "REAL":
        # TODO: replace with Riva gRPC streaming client
        # e.g., riva_asr_client.transcribe(audio_bytes)
        return "[REAL ASR not configured yet]"
    # MOCK: pretend user said a generic question
    return "Hi! Can you help me find today’s offers?"