# OpenAI Agent - Composio Integration for Claude AI Skills

Tres agentes IA listos para usar: OpenAI, Claude y Vercel/GitHub. Integrados con Composio para acceso a 500+ herramientas. 

## Agentes Disponibles

### 1. Agente OpenAI
**Archivo:** `agente_openai.py`

Agente basado en GPT-4 con acceso a:
- Gmail (enviar emails)
- Slack (enviar mensajes)
- GitHub (crear issues)
- Notion (crear páginas)
- Google Drive (listar archivos)

**Uso:**
```bash
python agente_openai.py
```

### 2. Agente Claude
**Archivo:** `agente_claude.py`

Agente basado en Claude 3.5 Sonnet con acceso a:
- Gmail
- Slack
- GitHub
- Notion

**Uso:**
```bash
python agente_claude.py
```

### 3. Agente Vercel
**Archivo:** `agente_vercel.py`

Agente especializado en despliegues y gestión de repositorios:
- Crear Pull Requests en GitHub
- Push de código
- Crear issues
- Obtener info de repositorios
- Desplegar a Vercel

**Uso:**
```bash
python agente_vercel.py
```

## Instalación

### Requisitos
- Python 3.8+
- pip

### Pasos de instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/gonzaloraknarok88/agent-openai.git
cd agent-openai
```

2. **Crear entorno virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus API keys
```

## Configuración de API Keys

Edita el archivo `.env` con tus credenciales:

- **OPENAI_API_KEY**: Obtener de https://platform.openai.com
- **ANTHROPIC_API_KEY**: Obtener de https://console.anthropic.com
- **COMPOSIO_API_KEY**: Obtener de https://composio.dev
- **VERCEL_TOKEN**: Obtener de https://vercel.com/account/tokens
- **GITHUB_TOKEN**: Obtener de GitHub Settings > Developer settings

## Uso Rápido

### OpenAI Agent
```python
from agente_openai import AgenteOpenAI

agente = AgenteOpenAI()
resultado = agente.ejecutar('Enviar email a cliente@ejemplo.com: El proyecto está listo')
print(resultado)
```

### Claude Agent
```python
from agente_claude import AgenteClaud

agente = AgenteClaud()
resultado = agente.ejecutar('Analiza mis últimos emails y crear un resumen en Notion')
print(resultado)
```

### Vercel Agent
```python
from agente_vercel import AgenteVercel

agente = AgenteVercel()
resultado = agente.ejecutar('Crear PR en mi repo de Next.js y desplegar a Vercel')
print(resultado)
```

## Conectar Cuentas con Composio

Para usar las herramientas de Composio, necesitas conectar tus cuentas:

```bash
pip install composio
composio configure
```

Sigue el flujo web para autorizar:
- Gmail
- Slack
- GitHub
- Notion
- Google Drive

## Estructura del Proyecto

```
agent-openai/
├── agente_openai.py       # Agente OpenAI
├── agente_claude.py       # Agente Claude
├── agente_vercel.py       # Agente Vercel
├── requirements.txt       # Dependencias
├── .env.example          # Plantilla de variables
└── README.md            # Este archivo
```

## Características

✅ 3 agentes IA diferentes (OpenAI, Claude, Vercel)
✅ Acceso a 500+ herramientas vía Composio
✅ Automatización de tareas comunes
✅ Integración con servicios populares
✅ Código limpio y modular
✅ Fácil de extender

## Archivos de Configuración

- `.env.example`: Plantilla con las variables requeridas
- `requirements.txt`: Todas las dependencias necesarias

## Notas de Seguridad

- **Nunca commitear .env**: El archivo .env está en .gitignore
- **Usa .env.example**: Como referencia para variables necesarias
- **Protege tus API keys**: No compartas tus tokens públicamente
- **Rotación de tokens**: Cambia tus tokens regularmente

## Licencia

MIT License - Siéntete libre de usar y modificar este código.

## Soporte

Para preguntas o problemas:
1. Revisa la documentación de Composio: https://docs.composio.dev
2. Documentación de OpenAI: https://platform.openai.com/docs
3. Documentación de Anthropic: https://docs.anthropic.com
4. Documentación de Vercel: https://vercel.com/docs

---

Creado por gonzaloraknarok88 | 2026
