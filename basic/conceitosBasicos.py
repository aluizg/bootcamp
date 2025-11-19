# Conceitos iniciais de Python
print("Bem vindo aos conceitos iniciais de Python")  # Exibe uma mensagem na tela
nome = input("Digite seu nome: ")  # Solicita ao usuário que digite seu nome
idade = int(input("Digite sua idade: "))  # Solicita ao usuário que digite sua idade

#f-string para formatar a saída com o nome do usuário
print(f"Olá, {nome}! Em 5 anos voces ira possuir {idade + 5} de idade")  # Saudação personalizada

if idade >= 18:  # Verifica se o usuário é maior de idade
    print("Você é maior de idade e pode acessar o site.")  # Mensagem para maiores de idade
else:
    print("Você é menor de idade e não pode acessar o site.")  # Mensagem para menores de idade
    exit()  # Encerra o programa se o usuário for menor de idade

#operacoes aritmeticas
num1 = float(input("Digite o primeiro número: "))  # Solicita o primeiro número
num2 = float(input("Digite o segundo número: "))  # Solicita o segundo número

print(f"A soma de {num1} e {num2} é {num1 + num2}")  # Exibe a soma
print(f"A subtração de {num1} e {num2} é {num1 - num2}")  # Exibe a subtração
print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")  # Exibe a multiplicação
print(f"A divisão de {num1} e {num2} é {num1 / num2}")  # Exibe a divisão 
print(f"O resto da divisão de {num1} por {num2} é {num1 % num2}")  # Exibe o resto da divisão
print(f"A potência de {num1} elevado a {num2} é {num1 ** num2}")  # Exibe a potência
print(f"A parte inteira da divisão de {num1} por {num2} é {num1 // num2}")  # Exibe a parte inteira da divisão