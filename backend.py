from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/chat/")
def chat(user_input: str):

    text = user_input.lower()

    # Smart Persona Detection
    technical_keywords = ["api", "error", "bug", "code", "server", "timeout"]
    frustrated_keywords = ["angry", "frustrated", "not working", "issue", "problem"]
    executive_keywords = ["roi", "revenue", "business", "impact", "loss", "profit"]

    technical_score = sum(word in text for word in technical_keywords)
    frustrated_score = sum(word in text for word in frustrated_keywords)
    executive_score = sum(word in text for word in executive_keywords)

    if technical_score >= frustrated_score and technical_score >= executive_score:
        persona = "technical"
    elif frustrated_score >= technical_score and frustrated_score >= executive_score:
        persona = "frustrated"
    elif executive_score >= technical_score and executive_score >= frustrated_score:
        persona = "executive"
    else:
        persona = "general"

    # Escalation
    if "refund" in text:
        ticket = random.randint(1000, 9999)
        return {
            "persona": persona,
            "response": f"Escalating to human agent. Ticket ID: {ticket}"
        }

    # Knowledge base search
    try:
        with open("kb.txt", "r") as f:
            lines = f.readlines()
    except:
        lines = []

    answer = "Please contact support."

    for line in lines:
        if any(word.lower() in line.lower() for word in text.split()):
            answer = line.strip()
            break

    # Tone adaptation
    if persona == "technical":
        final = f"Technical Explanation: {answer}"
    elif persona == "frustrated":
        final = f"I understand your frustration. {answer}"
    elif persona == "executive":
        final = f"From a business standpoint, {answer}"
    else:
        final = answer

    return {
        "persona": persona,
        "response": final
    }