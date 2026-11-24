class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True

    def descricao(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return (f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nStatus: {status}")

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

meu_livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
meu_livro2 = Livro("Capitães de Areia", "Jorge Amado", 342)
meu_livro3 = Livro("Harry Potter e a Pedra Filosofal", " J.K. Rowling", 264)

print(meu_livro.descricao())
print("-" * 80)

meu_livro3.emprestar()
print(meu_livro3.descricao())
print("-" * 80)

meu_livro2.devolver()
print(meu_livro2.descricao())