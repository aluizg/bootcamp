import buscaCEP as cep

def print_mensagem(mensagem="",tamanho=80):
    if mensagem:
        tamanho = len(mensagem) + 4
        print(mensagem.center(tamanho, "-"))
        
    for _ in range(tamanho):
        print("-", end="")
    print("\n")
    
def escolher_tipo_busca():
    while True:
        print("1. Buscar por CEP")
        print("2. Buscar por Logradouro")
        opcao = input("Digite o número da opção desejada: ")
        if opcao in ("1", "2"):
            return opcao
        print("Opção inválida. Tente novamente.\n")

def buscar_endereco():
    tipo_busca = escolher_tipo_busca()
    if tipo_busca == "1":
        return cep.busca_cep(input("Digite o CEP (somente números): "))
    elif tipo_busca == "2":
        return cep.busca_logradouro(
            input("Digite a rua\\avenida\\travessa: "),
            input("Digite a cidade: "),
            input("Digite o estado (UF): ")
        )

def endereco():
    while True:
        endereco = buscar_endereco()
        opcao = input(f"Endereço encontrado: {endereco}\nEstá correto? (s/n): ").lower()
        if opcao in ("s", "n"):
            if opcao == "s":
                return endereco
            else:
                print("Vamos tentar novamente.\n")
        else:
            print("Opção inválida. Tente novamente.\n")

print_mensagem("Bem-vindo ao sistema de busca de endereços e cálculo de rotas.")
print_mensagem("Informações dos dados de origem e destino são necessárias para calcular a rota.")
print("Dados do endereço de origem da rota de transporte:")

# Dados do endereço de origem da rota de transporte:
origem = endereco()
origem.update({"numero": input("Digite o número do endereço de origem: ")}) 
print(f"Endereço completo de origem: {origem['logradouro']}, {origem['numero']}, {origem['bairro']}, {origem['cidade']}-{origem['estado']}")

print("\nDados do endereço de destino da rota de transporte:")
destino = endereco()
destino.update({"numero": input("Digite o número do endereço de destino: ")}) 
print(f"Endereço completo de destino: {destino['logradouro']}, {destino['numero']}, {destino['bairro']}, {destino['cidade']}-{destino['estado']}")