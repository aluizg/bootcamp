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
                print("\nVamos tentar novamente.")
        else:
            print("Opção inválida. Tente novamente.\n")
            
def endereco_formatado(endereco_dict):
    return f"{endereco_dict['logradouro']}, {endereco_dict['numero']}, {endereco_dict['bairro']}, {endereco_dict['cidade']}, {endereco_dict['estado']}"       
