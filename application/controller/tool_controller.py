from application.model.entity.tools import Ferramenta
from application.model.dao.tools_Dao import Lista_Ferramentas
from flask import render_template,request
from application import app
import time


@app.route("/lista", methods=['GET'])
def listaFerramentas():
    return render_template("toolsList.html", Lista_Ferramentas=Lista_Ferramentas)

@app.route("/Adicionar", methods=['POST'])
def adicionar():
    time.sleep(3)
    id = len(Lista_Ferramentas) + 1
    nome = request.form.get('nome', None)
    site = request.form.get('site', None)
    descricao = request.form.get('descricao', None)
    ferramenta = Ferramenta(id, nome, site, descricao)
    Lista_Ferramentas.append(ferramenta)
    return render_template("toolsList.html", Lista_Ferramentas=Lista_Ferramentas)

@app.route("/buscar")
def buscar():
    Ferramentas_Filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    for Ferramenta in Lista_Ferramentas:
        if palavra_chave in Ferramenta.nome or palavra_chave in Ferramenta.descricao or palavra_chave in Ferramenta.__lista_tags:
            Ferramentas_Filtrado.append(Ferramenta)
    return render_template("todolist.html", todo_list=Ferramentas_Filtrado)