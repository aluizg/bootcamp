import funcoes
import pandas as pd
import re

df = funcoes.load_data('datasets', 'house.csv', 'csv')
print("Dados carregados com sucesso:")

# filter_df = df[(df['Rooms'] == 3) & (df['Type'] == 'h') & (df['Price'] <= 500000)]
# print(f'Casas com 3 quartos encontradas: {len(filter_df)}')

filter_street = df[df['Address'].str.contains('turner', flags=re.I)]
print(f"Casas localizadas em ruas (street): Exibindo as 10 primeiras de {len(filter_street)}")
print(filter_street[['Address', 'Rooms', 'Price']].head(10))