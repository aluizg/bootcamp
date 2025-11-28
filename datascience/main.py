import pandas as pd
import funcoes

dados = funcoes.load_data('datasets', 'fifa.csv', 'csv')    
print("Dados carregados com sucesso:")

#filtro pela quantidade de index informadas
print(dados.head(10))


# colunas do dataset
#print(f"Colunas do dataset: {dados.columns.tolist()}")

# coluna especifica
print("Nomes dos jogadores:")
print(dados[['Name','Nationality']].head(10))

#localizar valores especificos
brasil_players = dados.loc[dados['Nationality'] == 'Brazil']
print(f"Jogadores brasileiros encontrados: {len(brasil_players)}")
print(f"Jogadores brasileiros encontrados: {brasil_players[['Name', 'Club']].head(10)}")