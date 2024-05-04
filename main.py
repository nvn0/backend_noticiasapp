from flask import Flask, render_template, jsonify
from flask_cors import CORS
from azureapi import *
import json
import os

app = Flask(__name__)

CORS(app)


def carregar_json_para_dicionario(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo_json = json.load(arquivo)
    return conteudo_json


caminho_arquivo_json = 'noticias.json'
dicionario = carregar_json_para_dicionario(caminho_arquivo_json)
print(dicionario)

lista_final = []



for i in dicionario:      
    print(i)
    receber_classificacao = get_classification(i["Content"])
    print("clasificacao do azure:", receber_classificacao)
    
    classificacao = ""
    
    if receber_classificacao != 'Accept':
        classificacao = "Triste"
    else:
        classificacao = "Feliz"
    
    print(classificacao)

    resposta = {
        "Title":i["Title"],
        "Classification": classificacao,
        "Content": i["Content"],
        "URL": i["URL"]
    }
    
    lista_final.append(resposta)
    print(lista_final)
    
    print("Final", resposta)



@app.route('/')
def homepage():
    return 'The API is running...'


@app.route('/resposta1')
def resposta1():

    
    
    return jsonify(lista_final)


@app.route('/resposta2')
def resposta2():
    
    return '<p>Olá</p>'
    #return render_template("file.html")


app.run()
