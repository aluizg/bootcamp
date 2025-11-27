def cozimento_c(temperatura):
    if temperatura < 48:
        return "crua"
    elif temperatura in range(48, 53):
        return "selada"
    elif temperatura in range(54, 59):
        return "ao ponto para mal"
    elif temperatura in range(60, 64):
        return "ao ponto"
    elif temperatura in range(65, 70):
        return "ao ponto para bem"
    else:
        return "bem passada"

def cozimento_f(temperatura):
    if temperatura < 120:
        return "crua"
    elif 120 <= temperatura < 130:
        return "selada"
    elif 130 <= temperatura < 140:
        return "ao ponto para mal"
    elif 140 <= temperatura < 150:
        return "ao ponto"
    elif 150 <= temperatura < 160:
        return "ao ponto para bem"
    else:
        return "bem passada"

def main():
    escala = input("Digite a escala de temperatura (C/F): ").strip().upper()
    
    if escala not in ['C', 'F']:
        print("Escala inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
        return
    
    temperatura = int(input("Digite a temperatura da carne: "))
    
    match escala:
        case 'C':
            resultado = cozimento_c(temperatura)
        case 'F':
            resultado = cozimento_f(temperatura)
        case _:
            print("Erro inesperado.")
            return

    print(f"Nível de cozimento: {resultado}")
    
main()