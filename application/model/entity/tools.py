from typing import List
from application.model.entity.tag import Tag

class Ferramenta:
    def __init__(self, nome:str, site:str, lista_tags: List[tag]):
        self.__nome = nome
        self.__site = site
        self.__lista_tags = lista_tags
        
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
def tag(self):
    return self.__tag

@tag.setter
def tag(self,valor):
    self.__tag = valor
    
    