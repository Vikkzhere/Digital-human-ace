import os, json, urllib.request

def llm_chat(user_text: str) -> str:
    mode = os.getenv("MODE","MOCK").upper()
    if mode == "REAL":
        # Minimal REST example for NIM LLM endpoint (OpenAI-compatible schema)
        url = os.getenv("NIM_LLM_URL","")
        api_key = os.getenv("NIM_LLM_API_KEY","")
        if url and api_key:
            data = {
                "model": "nemotron", 
                "messages": [{"role":"user","content":user_text}],
                "temperature": 0.5,
            }
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"))
            req.add_header("Content-Type","application/json")
            req.add_header("Authorization", f"Bearer {api_key}")
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    j = json.loads(resp.read().decode("utf-8"))
                    # OpenAI-compatible: choices[0].message.content
                    return j.get("choices",[{}])[0].get("message",{}).get("content","(no content)")
            except Exception as e:
                return f"[REAL LLM error: {e}]"
        return "[REAL LLM not configured]"
    # MOCK: simple domain-specific reply
    if any(k in user_text.lower() for k in ["refund","return","policy"]):
        return "Sure — you can return items within 30 days with the receipt. Would you like me to generate a QR for drop-off?"
    if any(k in user_text.lower() for k in ["offer","deal","discount"]):
        return "Today’s top offers: 20% off accessories and free shipping on orders over €50."
    return "I’m your virtual assistant. Ask me about store hours, returns, or today’s offers."
