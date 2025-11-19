# from <nome doe arquivo> import <nome da funcao>
# from duracaoProduto import calcular_duracao_produto
# ----------------------------------------------------
# importando todas as funcos de um arquivo
# from basic.funcoes import *
from basic import funcoes
from basic.utilidades import utils as util
from dataclass import usuario, heranca

# usando as funcoes importadas
# nome = input("Digite seu nome: ")
# email = input("Digite seu email: ")
# idade = int(input("Digite sua idade: "))

usuario1 = usuario.Usuario(
    nome=input("Digite seu nome: "),
    email=input("Digite seu email: "),
    idade=int(input("Digite sua idade: "))
)

print(funcoes.saudacao(usuario1.nome))
util.informacoes()

if funcoes.maior_idade(usuario1.idade):
    print("Acesso liberado. Você é maior de idade.")
else:
    print("Acesso negado. Você é menor de idade.")
    exit()

cachorro1 = heranca.Cachorro("Rex", "marrom", "cachorro")
cachorro1.apresentar()
