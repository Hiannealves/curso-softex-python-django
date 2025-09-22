#1
class Pessoa:
    def __init__(self, nome:str,idade:int):
        self._nome = nome
        self._idade = idade

        p1 = Pessoa("Hianne",37)
        p2 = Pessoa("Natã", 12)
#2
    @property
    def nome(self):
        return self._nome
    #3
    @nome.setter 
    def nome (self, novo_nome:str):
        if isinstance (novo_nome,str) and novo_nome:
            self._nome = novo_nome
            print(novo_nome)
        else:
            print("Erro: Escreva um nome válido")
    #4
    @property
    def idade(self):
        return self._idade
    #5
    @idade.setter
    def idade(self, nova_idade:int):
        if isinstance (nova_idade > 0 and nova_idade(int)):
            self._idade = nova_idade
        print(nova_idade)

 
