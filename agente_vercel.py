#!/usr/bin/env python3
# AGENTE 3 - Vercel/GitHub + Composio
# Ejecuta: python agente_vercel.py

import os
from composio_openai import ComposioToolSet, Action
from openai import OpenAI
import requests

class AgenteVercel:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.composio = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))
        self.vercel_token = os.getenv('VERCEL_TOKEN')
        self.github_token = os.getenv('GITHUB_TOKEN')
    
    def obtener_tools(self):
        """Obtiene tools para GitHub y Vercel"""
        return self.composio.get_tools(actions=[
            Action.GITHUB_CREATE_PULL_REQUEST,
            Action.GITHUB_PUSH_CODE,
            Action.GITHUB_CREATE_ISSUE,
            Action.GITHUB_GET_REPO_INFO,
        ])
    
    def desplegar_vercel(self, proyecto):
        """Despliega a Vercel via API"""
        url = 'https://api.vercel.com/v13/deployments'
        headers = {'Authorization': f'Bearer {self.vercel_token}'}
        
        data = {
            'name': proyecto,
            'githubDeploymentUrlQuery': 'buildCommand=npm+run+build'
        }
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    def ejecutar(self, prompt):
        """Ejecuta el agente para manejo de repos y deploys"""
        tools = self.obtener_tools()
        
        response = self.client.chat.completions.create(
            model='gpt-4-turbo',
            tools=tools,
            messages=[{'role': 'user', 'content': prompt}]
        )
        
        return response

if __name__ == '__main__':
    agente = AgenteVercel()
    resultado = agente.ejecutar('Crear PR en mi repo de Next.js y desplegar a Vercel')
    print(resultado)
