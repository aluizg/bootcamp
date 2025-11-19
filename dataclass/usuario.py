class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}, Idade: {self.idade}")