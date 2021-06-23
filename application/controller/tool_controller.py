from application.model.entity.tools import Ferramenta
from application.model.dao.tools_Dao import Lista_Ferramentas
from flask import render_template,request
from application import app
import time


@app.route("/lista", methods=['GET'])
def listaFerramentas():
    return render_template("toolsList.html", Lista_Ferramentas=Lista_Ferramentas)

@app.route("/adicionar", methods=['POST'])
def adicionar():
    id = len(Lista_Ferramentas) + 1
    nome = request.form.get('nome', None)
    site = request.form.get('site', None)
    descricao = request.form.get('descricao', None)
    tags = request.form.get('tags', None)
    ferramenta = Ferramenta(id, nome, site, descricao, tags)
    Lista_Ferramentas.append(ferramenta)
    return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas)

@app.route("/buscar", methods=['GET'])
def buscar():
    Ferramentas_Filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    for Ferramenta in Lista_Ferramentas:
        if palavra_chave in Ferramenta.nome or palavra_chave in Ferramenta.descricao or palavra_chave in Ferramenta.tags:
            Ferramentas_Filtrado.append(Ferramenta)
    return render_template("toolsList.html", Lista_Ferramentas=Ferramentas_Filtrado)

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id: int):
    if request.method == 'GET':
        for Ferramenta in Lista_Ferramentas:
            if Ferramenta.id == id:
                return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas, Ferramenta_editar=Ferramenta)
        return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas), 404
    else:
        nome = request.form.get('nome', None)
        site = request.form.get('site', None)
        descricao = request.form.get('descricao', None)
        tags = request.form.get('tags', None)
        for Ferramenta in Lista_Ferramentas:
            if Ferramenta.id == id:
                Ferramenta.nome = nome
                Ferramenta.site = site
                Ferramenta.descricao = descricao
                Ferramenta.tags = tags
        return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas)

@app.route("/remover/<int:id>", methods=['GET'])
def remover(id: int):
    for tool in Lista_Ferramentas:
        if tool.id == id:
            Lista_Ferramentas.remove(tool)
            return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas)
    return render_template("home.html", Lista_Ferramentas=Lista_Ferramentas), 404
