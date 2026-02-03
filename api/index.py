from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="AI Agents API - Vercel",
    description="Agentes OpenAI, Claude y Vercel con Composio Integration",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Agents API",
        "version": "1.0.0",
        "deployment": "Vercel"
    }

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI Agents API - DEPLOYADO EN VERCEL",
        "status": "online",
        "endpoints": {
            "health": "/api/health",
            "docs": "/docs",
            "redoc": "/redoc"
        },
        "info": "API lista para usar. Agregar variables de entorno en Vercel para OpenAI, Anthropic y Composio"
    }

# OpenAI endpoint (placeholder)
@app.get("/api/openai")
def openai_agent(prompt: str = "Hello"):
    return {
        "agent": "openai",
        "prompt": prompt,
        "status": "Agent ready. Requires OPENAI_API_KEY environment variable."
    }

# Claude endpoint (placeholder)
@app.get("/api/claude")
def claude_agent(prompt: str = "Hello"):
    return {
        "agent": "claude",
        "prompt": prompt,
        "status": "Agent ready. Requires ANTHROPIC_API_KEY environment variable."
    }

# Vercel endpoint (placeholder)
@app.get("/api/vercel")
def vercel_agent(prompt: str = "Hello"):
    return {
        "agent": "vercel",
        "prompt": prompt,
        "status": "Agent ready. Requires VERCEL_TOKEN and GITHUB_TOKEN environment variables."
    }

# API status
@app.get("/status")
def status():
    return JSONResponse({
        "deployment": "Vercel",
        "status": "Online",
        "timestamp": "2026-02-03",
        "agents": ["openai", "claude", "vercel"]
    })
