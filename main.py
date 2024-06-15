from flask import Flask, render_template, jsonify
from flask_cors import CORS
from azureapi import *
from query import *
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
lista_temp = []

def get_noticias():

    while True:
        #lista_final.clear()
        
        try:
            r = requests.get("https://newsdata.io/api/1/latest?apikey=pub_46252bc7b72ef0d7a12c35b8bf4b299bb2090&language=pt")
            print(r)

        except:
            print("erro ao aceder à api")
        else:
            data = r.json()
            print(data)
            
            max_results = 12
            results = data.get('results', [])
            for result in results[:max_results]:
                #link = result['link']
                #title = result['title']
                #description = result['description']
                
                
                noticia = {
                    "Title": result['title'],
                    "Classification": "",
                    "Content": result['description'],
                    "URL": result['link']
                }
            
                lista_temp.append(noticia)
                
        print(lista_temp)
        Classificar()
        time.sleep(700)
        
        
        #dicionario.clear()












def Classificar():

    for i in lista_temp:         
        
        classificacao = Classificacao_llama3(i["Content"])    

        
        print(classificacao)

        noticia = {
            "Title":i["Title"],
            "Classification": classificacao,
            "Content": i["Content"],
            "URL": i["URL"]
        }
        
        lista_final.append(noticia)
        
   
    time.sleep(20)


def classificar_dict_estatico():

    for i in dicionario:      
        

        #receber_classificacao = ""
        #receber_classificacao = get_classification(i["Content"])
        #print("clasificacao do azure:", receber_classificacao)
        
        classificacao = Classificacao_llama3(i["Content"])
        
        
        #if receber_classificacao != 'Accept':
        #    classificacao = "Triste"
        #else:
        #    classificacao = "Feliz"
        
        
        # temp só pra nao gastar dinheiro do azure
        #if x % 2 == 0:
        #    classificacao = "Triste"
        #else:
        #    classificacao = "Feliz"
        
        
        
        print(classificacao)

        noticia = {
            "Title":i["Title"],
            "Classification": classificacao,
            "Content": i["Content"],
            "URL": i["URL"]
        }
        
        lista_final.append(noticia)
        
        #x += 1
        
        #print(lista_final)
        
        #print("Final", resposta)
       



noticias_felizes = []
noticias_tristes = []

def filtrar_noticias():

    while True:

        noticias_felizes.clear()
        noticias_tristes.clear()


        for obj in lista_final:
            # Verificar o valor do parâmetro "Classification"
            if obj["Classification"] == "Feliz":
                noticias_felizes.append(obj)
            elif obj["Classification"] == "Triste":
                noticias_tristes.append(obj)
                
        time.sleep(720)









#threading.Thread(target=get_noticias, daemon=True).start()
#threading.Thread(target=filtar_noticias, daemon=True).start()
#threading.Thread(target=classiificar, daemon=True).start()


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



if __name__ == '__main__':
    #app.run()
    classificar_dict_estatico()
    threading.Thread(target=get_noticias, daemon=True).start()
    #threading.Thread(target=filtrar_noticias, daemon=True).start()
    app.run()
    #app.run(host='0.0.0.0' , port=5000)
    
    
    
    
    
    
    
    
    