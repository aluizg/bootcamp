def potencia(base, expoente=2):
    return base ** expoente

base = int(input("Digite a base: "))
expoente = input("Digite o expoente (pressione Enter para usar o valor padrão 2): ")

resultado = potencia(base, int(expoente)) if expoente else potencia(base)
print(f"{base} elevado a {expoente or 2} é igual a {resultado}")