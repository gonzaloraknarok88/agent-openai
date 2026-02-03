from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from agente_openai import AgenteOpenAI
from agente_claude import AgenteClaud
from agente_vercel import AgenteVercel

load_dotenv()

app = FastAPI(
    title="AI Agents API",
    description="OpenAI, Claude y Vercel Agents con Composio",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Agents API",
        "version": "1.0.0"
    }

# OpenAI Agent
@app.post("/api/openai")
def ejecutar_openai(prompt: str):
    try:
        agente = AgenteOpenAI()
        resultado = agente.ejecutar(prompt)
        return {
            "agent": "openai",
            "prompt": prompt,
            "response": str(resultado),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Claude Agent
@app.post("/api/claude")
def ejecutar_claude(prompt: str):
    try:
        agente = AgenteClaud()
        resultado = agente.ejecutar(prompt)
        return {
            "agent": "claude",
            "prompt": prompt,
            "response": str(resultado),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Vercel Agent
@app.post("/api/vercel")
def ejecutar_vercel(prompt: str):
    try:
        agente = AgenteVercel()
        resultado = agente.ejecutar(prompt)
        return {
            "agent": "vercel",
            "prompt": prompt,
            "response": str(resultado),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root
@app.get("/")
def root():
    return {
        "message": "AI Agents API - Desplegada en Vercel",
        "endpoints": {
            "health": "/api/health",
            "openai": "/api/openai?prompt=tu_prompt",
            "claude": "/api/claude?prompt=tu_prompt",
            "vercel": "/api/vercel?prompt=tu_prompt"
        },
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
