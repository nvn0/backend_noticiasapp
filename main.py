from flask import Flask, render_template, jsonify
from flask_cors import CORS
from azureapi import *
import json
import os
import time
import requests
import threading

app = Flask(__name__)

CORS(app)


def carregar_json_para_dicionario(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo_json = json.load(arquivo)
    return conteudo_json


caminho_arquivo_json = 'noticias.json'
dicionario = carregar_json_para_dicionario(caminho_arquivo_json)
print("DICIONARIO: ", dicionario)

lista_final = []


def get_noticias():

    

    try:
        r = requests.get("api_url")
        print(r)


        dados = r.json()
        print(dados)
    except:
        print("erro ao aceder à api")
    else:
        noticia = {
            "Title":dados["Title"],
            "Classification": "",
            "Content": dados["Content"],
            "URL": dados["URL"]
        }
        
        lista_final.append(noticia)
        
    time.sleep(700)
    
    lista_final.clear()










x = 10

for i in dicionario:      


    receber_classificacao = ""
    #receber_classificacao = get_classification(i["Content"])
    #print("clasificacao do azure:", receber_classificacao)
    
    classificacao = ""
    
    #if receber_classificacao != 'Accept':
    #    classificacao = "Triste"
    #else:
    #    classificacao = "Feliz"
    
    
    
    if x % 2 == 0:
        classificacao = "Triste"
    else:
        classificacao = "Feliz"
    
    #print(classificacao)

    noticia = {
        "Title":i["Title"],
        "Classification": classificacao,
        "Content": i["Content"],
        "URL": i["URL"]
    }
    
    lista_final.append(noticia)
    x += 1
    print(x)
    print(lista_final)
    
    #print("Final", resposta)



noticias_felizes = []
noticias_tristes = []

def filtar_noticias():

    noticias_felizes.clear()
    noticias_tristes.clear()


    for obj in lista_final:
        # Verificar o valor do parâmetro "Classification"
        if obj["Classification"] == "Feliz":
            noticias_felizes.append(obj)
        elif obj["Classification"] == "Triste":
            noticias_tristes.append(obj)
            
    time.sleep(720)









threading.Thread(target=get_noticias, daemon=True).start()
threading.Thread(target=filtar_noticias, daemon=True).start()


@app.route('/')
def homepage():
    return 'The API is running...'


@app.route('/noticias')
def noticias():

    
    
    
    return jsonify(lista_final)


@app.route('/feliz')
def nfelizes():
    
    
    
    
    return jsonify(noticias_felizes)
    
    
@app.route('/triste')
def ntristes():
    
    
    time.sleep(3)
    
    return jsonify(noticias_tristes)


app.run()
