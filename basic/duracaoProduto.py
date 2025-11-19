#Calcular quantos dias um produto dura baseado na quantidade de uso diário.
def calcular_duracao_produto(quantidade_total, uso_diario):
    if uso_diario <= 0:
        raise ValueError("O uso diário deve ser maior que zero.")
    return quantidade_total // uso_diario

#obtem informacoes do usuario
quantidade_total = int(input("Digite a quantidade total do produto (em unidades): "))
uso_diario = int(input("Digite a quantidade usada por dia (em unidades): "))
duracao = calcular_duracao_produto(quantidade_total, uso_diario)
print(f"O produto durará aproximadamente {duracao:.0f} dias.")