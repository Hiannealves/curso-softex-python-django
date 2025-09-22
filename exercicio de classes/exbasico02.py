class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print("Pessoa 1:", p1.nome, "-", p1.idade, "anos")
print("Pessoa 2:", p2.nome, "-", p2.idade, "anos")
