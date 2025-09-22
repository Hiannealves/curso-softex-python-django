class Funcionario:
    percentual_bonus = 1.10  # atributo de classe

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"{self.nome} agora recebe R${self.salario:.2f}")

f1 = Funcionario("Carlos", 2000)
f2 = Funcionario("Ana", 3000)

f1.aplicar_bonus()
f2.aplicar_bonus()
