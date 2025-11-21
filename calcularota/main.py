import dadosRota as rota
import utils as util

util.print_mensagem("Bem-vindo ao sistema de busca de endereços e cálculo de rotas.")
util.print_mensagem("Informações dos dados de origem e destino são necessárias para calcular a rota.")
print("Dados do endereço de origem da rota de transporte:")

# Dados do endereço de origem da rota de transporte:
origem = util.endereco()
origem.update({"numero": input("Digite o número do endereço de origem: ")}) 
print(f"Endereço completo de origem: {util.endereco_formatado(origem)}")

print("\nDados do endereço de destino da rota de transporte:")
destino = util.endereco()
destino.update({"numero": input("Digite o número do endereço de destino: ")}) 
print(f"Endereço completo de destino: {util.endereco_formatado(destino)}\n")

util.print_mensagem("Cálculo da rota entre os endereços informados")
distancia, duracao = rota.get_info_rota(
    util.endereco_formatado(origem),
    util.endereco_formatado(destino)
)
if distancia and duracao:
    print(f"Distância: {distancia}, Duração: {duracao}")
else:
    print("Não foi possível calcular a rota com os endereços informados.")