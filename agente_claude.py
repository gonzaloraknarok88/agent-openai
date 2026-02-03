#!/usr/bin/env python3
# AGENTE 2 - Claude + Composio
# Ejecuta: python agente_claude.py

import os
from composio_tools import Tool, ComposioToolSet
from anthropic import Anthropic

class AgenteClaud:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.composio = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))
    
    def obtener_tools(self):
        """Obtiene herramientas para analizar datos"""
        return self.composio.get_tools(apps=[
            'gmail',
            'slack',
            'github',
            'notion',
        ])
    
    def ejecutar(self, prompt):
        """Ejecuta el agente Claude con tools"""
        tools = self.obtener_tools()
        
        response = self.client.messages.create(
            model='claude-3-5-sonnet-20241022',
            max_tokens=2048,
            tools=tools,
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        
        return response

if __name__ == '__main__':
    agente = AgenteClaud()
    resultado = agente.ejecutar('Analiza mis ultimos emails y crear un resumen en Notion')
    print(resultado)
