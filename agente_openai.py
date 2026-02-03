#!/usr/bin/env python3
# AGENTE 1 - OpenAI + Composio
# Ejecuta: python agente_openai.py

import os
from composio_openai import ComposioToolSet, Action
from openai import OpenAI

class AgenteOpenAI:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.composio = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))
    
    def obtener_tools(self):
        """Obtiene las 500+ herramientas de Composio"""
        return self.composio.get_tools(actions=[
            Action.GMAIL_SEND_EMAIL,
            Action.SLACK_SEND_MESSAGE,
            Action.GITHUB_CREATE_ISSUE,
            Action.NOTION_CREATE_PAGE,
            Action.GOOGLE_DRIVE_LIST_FILES,
        ])
    
    def ejecutar(self, prompt):
        """Ejecuta el agente con un prompt"""
        tools = self.obtener_tools()
        
        response = self.client.chat.completions.create(
            model='gpt-4-turbo',
            tools=tools,
            messages=[{'role': 'user', 'content': prompt}]
        )
        
        return response

if __name__ == '__main__':
    agente = AgenteOpenAI()
    resultado = agente.ejecutar('Enviar email a cliente@ejemplo.com: El proyecto esta listo')
    print(resultado)
