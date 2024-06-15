import subprocess
#import pexpect
import time
import requests
import json

# https://ollama.com

# curl -fsSL https://ollama.com/install.sh | sh

#curl http://localhost:11434/api/generate -d '{
#  "model": "llama3",
#  "prompt": "Why is the sky blue?",
#  "stream": false
#}'



def Classificacao_llama3(frase):
    
    prompt = f"Classifica esta frase com o sentimento mais provavel escreve apenas a palavra: '{frase}' "

    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        content = response.json()  # Return the response as JSON
        return content["response"]
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
 
    

    