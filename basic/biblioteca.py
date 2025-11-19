class Livro:
    def __init__(self, titulo, autor, ano, assunto):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.assunto = assunto

    def detalhes(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano}, assunto: {self.assunto}"
    
class Secao:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(livro.detalhes())
        print("\n")
    
class Biblioteca(Secao):
    def __init__(self, nome):
        super().__init__(nome)
        self.secoes = {}

    def adicionar_secao(self, secao):
        self.secoes[secao.nome] = secao

    def listar_secoes(self):
        print("Seções na biblioteca:\n")
        for secao in self.secoes.values():
            print(secao.nome)
            secao.listar_livros()

# Exemplo de uso
ficcao = Secao("Ficção")
ficcao.adicionar_livro(Livro("1984", "George Orwell", 1949, "Distopia"))
ficcao.adicionar_livro(Livro("Brave New World", "Aldous Huxley", 1932, "Distopia"))

ciencia = Secao("Ciência")
ciencia.adicionar_livro(Livro("A Brief History of Time", "Stephen Hawking", 1988, "Cosmologia"))

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.adicionar_secao(ficcao)
biblioteca.adicionar_secao(ciencia)
biblioteca.listar_secoes()