PROJECT: Persona-Adaptive Customer Support Agent

Objective:
To build a customer support system that:
- Detects customer persona
- Retrieves relevant knowledge base answers
- Adapts response tone
- Escalates to human agent when required

Architecture Flow:
User → Streamlit UI → FastAPI Backend → Persona Detection → 
Escalation Check → Knowledge Base Search → Tone Adaptation → Response

Features:
- Smart persona detection using keyword scoring
- Knowledge base retrieval from external file (kb.txt)
- Tone adaptation based on persona
- Random ticket ID generation for escalation
- Backend API using FastAPI
- Frontend demo using Streamlit

How to Run:
1. Activate conda environment:
   conda activate persona_agent

2. Run backend:
   uvicorn backend:app --reload

3. Run frontend:
   streamlit run app.py

Future Improvements:
- LLM-based persona classification
- Vector embedding-based semantic search
- CRM integration for real escalation