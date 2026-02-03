#!/bin/bash

echo "====================================="
echo "OpenAI Agent - Composio Setup Script"
echo "====================================="
echo ""

# Crear entorno virtual
echo "[1/4] Creando entorno virtual..."
if [ -d ".venv" ]; then
    echo "Entorno virtual ya existe"
else
    python3 -m venv .venv
    echo "Entorno virtual creado"
fi

# Activar entorno virtual
echo "[2/4] Activando entorno virtual..."
source .venv/bin/activate

# Instalar dependencias
echo "[3/4] Instalando dependencias..."
pip install -r requirements.txt

# Crear archivo .env
echo "[4/4] Configurando variables de entorno..."
if [ -f ".env" ]; then
    echo "Archivo .env ya existe"
else
    cp .env.example .env
    echo "Archivo .env creado desde .env.example"
    echo ""
    echo "*** IMPORTANTE ***"
    echo "Edita el archivo .env con tus API keys:"
    echo "  - OPENAI_API_KEY"
    echo "  - ANTHROPIC_API_KEY"
    echo "  - COMPOSIO_API_KEY"
    echo "  - VERCEL_TOKEN (opcional)"
    echo "  - GITHUB_TOKEN (opcional)"
fi

echo ""
echo "====================================="
echo "Setup completado!"
echo "====================================="
echo ""
echo "Pasos siguiente:"
echo "1. Edita .env con tus API keys"
echo "2. Ejecuta: source .venv/bin/activate"
echo "3. Ejecuta: python agente_openai.py"
echo "           o python agente_claude.py"
echo "           o python agente_vercel.py"
echo ""
echo "Para conectar tus cuentas con Composio:"
echo "  pip install composio"
echo "  composio configure"
echo ""
echo "Documentación: https://docs.composio.dev"
echo ""
