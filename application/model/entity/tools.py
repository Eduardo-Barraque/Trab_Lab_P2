from typing import List

class Ferramenta:
    def __init__(self, id:str, nome:str, site:str, descricao:str, tags):
        self.__id = id
        self.__nome = nome
        self.__site = site
        self.__descricao = descricao
        self.__tags = tags
            
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor       
            
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,valor):
        self.__nome = valor

    @property
    def site(self):
        return self.__site

    @site.setter
    def site(self,valor):
        self.__site = valor

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self,valor):
        self.__tags = valor
    
    