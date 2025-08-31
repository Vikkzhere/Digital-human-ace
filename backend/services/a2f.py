import os, json
def audio_to_visemes(wav_bytes: bytes):
    mode = os.getenv("MODE","MOCK").upper()
    if mode == "REAL":
        # TODO: POST wav_bytes to Audio2Face NIM and return blendshapes/visemes
        return [{"t": i*0.1, "v": 0.5} for i in range(10)]
    # MOCK: simple sawtooth visemes over ~0.8s
    vis = []
    t = 0.0
    for i in range(16):
        vis.append({"t": round(t,3), "v": (i%4)/3.0})
        t += 0.05
    return vis
