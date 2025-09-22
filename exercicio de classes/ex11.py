class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        for livro in self.acervo:
            print(f"{livro.titulo} - {livro.autor}")

bib = Biblioteca()
l1 = Livro("1984", "George Orwell")
l2 = Livro("Dom Casmurro", "Machado de Assis")
l3 = Livro("The secret", "Rhondo Byrne")

bib.adicionar_livro(l1)
bib.adicionar_livro(l2)
bib.adicionar_livro(l3)
bib.listar_livros()
