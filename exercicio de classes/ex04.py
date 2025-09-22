class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto("Caderno", 15.50)
p2 = Produto("Caneta", 3.00)

print("Produto:", p1.nome, "- R$", p1.preco)
print("Produto:", p2.nome, "- R$", p2.preco)

