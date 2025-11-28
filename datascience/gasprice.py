from funcoes import load_data, save_graph
import matplotlib.pyplot as plt
import numpy as np

df = load_data('datasets', 'gas_prices.csv', 'csv')
print("Dados carregados com sucesso:")

plt.title('Valores do combustível ao longo dos anos em dolares')
# plt.plot(df['Year'], df['Australia'], 'k.--', marker='o', label='AUS')
# plt.plot(df['Year'], df['Italy'], marker='o', label='ITA')
# plt.plot(df['Year'], df['USA'], marker='o', label='USA')
# plt.plot(df['Year'], df['Japan'], marker='o', label='JPA')

# paises = ['Australia', 'Italy', 'USA', 'Japan', 'France', 'Canada', 'Germany']
# for pais in df:
#     if pais in paises:
#         plt.plot(df['Year'], df[pais], marker='o', label=pais)

paises = {
    'Australia': 'AUS', 
    'Italy': 'ITA', 
    'USA': 'USA',
    'Japan': 'JPA',
    'France': 'FRA',
    'Canada': 'CAN',
    'Germany': 'GER'
}
for pais in df:
    if pais in paises:
        plt.plot(df['Year'], df[pais], marker='o', label=paises[pais])
        
#dados de eixo x
plt.xlabel('Ano')
plt.xticks(df['Year'][::5])  # Mostra um tick a cada 5 anos)
#plt.xticks(np.arange(df['Year'].min(), df['Year'].max()+1, 5))

#dadod do eixo y
plt.ylabel('$USD')

# para exibir as legendas
plt.legend()

#salvar o grafico
save_graph(plt, 'datasets', 'gas_prices.png')

#mostrar o grafico
plt.show()

