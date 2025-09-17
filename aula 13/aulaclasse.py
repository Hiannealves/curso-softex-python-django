"""classe é um molde para criar objetos.
classes sempre se usa letras maiúsculas.
"""
class Cachorro:
# Esta função especial roda toda vez que um novo cachorro é criado.
    def __init__ (self, nome_do_cao, cor_do_pelo):
        print(f"Um novo cachorro chamado {nome_do_cao} nasceu!")
# Vamos guardar essas informações no próximo slide ...
class Cachorro:
   def __init__ (self, nome_do_cao, cor_do_pelo):
# "O nome DESTE cachorro será ... "
    self.nome = nome_do_cao
# "A cor DESTE cachorro será ... "
    self.cor = cor_do_pelo

class Cachorro:
   def __init__ (self, nome_do_cao, cor_do_pelo):
# "O nome DESTE cachorro será ... "
    self.nome = nome_do_cao
# "A cor DESTE cachorro será ... "
    self.cor = cor_do_pelo
 
"""Além de características, podemos ensinar "ações" para nossos objetos. Essas ações são chamadas de Métodos.

Métodos são funções que ficam dentro do molde.
 """
class Cachorro:
    def __init__ (self, nome_do_cao, cor_do_pelo):
        self.nome = nome_do_cao
        self.cor = cor_do_pelo
# Isto é um método. Uma ação que o cachorro pode fazer.
    def latir(self) :
        print (f"{self.nome} diz: Au au!")

# Criando os cachorros novamente
        rex = Cachorro("Rex", "Marrom")
        bela = Cachorro("Bela", "Branca")
# Pedindo para cada um deles latir
        rex. latir() # Saída: Rex diz: Au au!
        bela. latir() # Saída: Bela diz: Au au!

# O MOLDE COMPLETO
class Cachorro:
# 1. Registro de nascimento com as CARACTERÍSTICAS (Atributos)
    def __init__ (self, nome, cor) :
      self.nome = nome
      self.cor = cor
# 2. AÇÃO que ele sabe fazer (Método)
def latir(self) :
    print(f"{self.nome} diz: Au au!")
# USANDO O MOLDE
    meu_cachorro = Cachorro("Bidu", "Azul")
    print(f"Meu cachorro se chama {meu_cachorro.nome}. ")
    meu_cachorro. latir()

