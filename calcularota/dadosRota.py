import requests as resquest
import environment as env

def get_info_rota(origem, destino):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origem,
        "destination": destino,
        "key": env.get_api_key()
    }
    response = resquest.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            route = data['routes'][0]['legs'][0]
            distancia = route['distance']['text']
            duracao = route['duration']['text']
            return distancia, duracao
        else:
            print(f"Erro na API: {data['status']}")
    else:
        print(f"Erro na requisição: {response.status_code}")
    return None, None
    
# ponto_origem = "Rua Piauí, 400, Todos os Santos, RJ"
# ponto_destino = "Rua Tenório Cavalcanti, 80, Nova Iguaçu, RJ"
# distancia, duracao = get_info_rota(ponto_origem, ponto_destino)
# print(f"Distância: {distancia}, Duração: {duracao}")
