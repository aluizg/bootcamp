def calc_metro_quadrado(largura, comprimento):
    return largura * comprimento

def quantidade_tinta(redimento_m2, area):
    return area / redimento_m2

def main():
    largura = float(input("Digite a largura da parede (em metros): "))
    comprimento = float(input("Digite o comprimento da parede (em metros): "))
    rendimento_m2 = float(input("Digite o rendimento da lata de tinta (m² por litro): "))
    
    area = calc_metro_quadrado(largura, comprimento)
    litros_necessarios = quantidade_tinta(rendimento_m2, area)
    
    print(f"Área da parede: {area:.1f} m²")
    print(f"Litros de tinta necessários: {litros_necessarios:.1f} litros")

main()