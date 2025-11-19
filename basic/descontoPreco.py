# conceder desconto baseado no preço do produto
preco = float(input("Digite o preço do produto (R$): "))  # Solicita o preço do produto  
desconto = float(input("Digite a porcentagem de desconto (%): "))  # Solicita a porcentagem de desconto
preco_final = preco - (preco * desconto / 100)  # Calcula o preço final com desconto
print(f"O preço final do produto com desconto é: R$ {preco_final:.2f}")  # Exibe o preço final formatado com duas casas decimais