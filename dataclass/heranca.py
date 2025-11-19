class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f"Olá, eu sou um {self.especie} chamado {self.nome} e minha cor é {self.cor}.")
        
class Gato(Animal):
    pass

    def miar(self):
        print(f"{self.nome} está miando!")

class Cachorro(Animal):
    pass

    def latir(self):
        print(f"{self.nome} está latindo!")
        
        
class Passaro(Animal):
    def __init__(self, nome, cor, especie, pode_voar):
        super().__init__(nome, cor, especie)
        self.pode_voar = pode_voar        


gato1 = Gato("Whiskers", "cinza", "gato")
gato1.apresentar()
gato1.miar()