import requests as request

def valida_cep(cep):
    cep = cep.replace("-", "").replace(".", "").replace(" ", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP inválido. Deve conter 8 dígitos numéricos.")
    return cep

def busca_cep(cep):
    cep = valida_cep(cep)
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = request.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Erro na requisição: {response.status_code}")
    data = response.json()
    if "erro" in data:
        raise ValueError("CEP não encontrado.")
    return {
        "logradouro": data.get("logradouro", ""),
        "bairro": data.get("bairro", ""),
        "cidade": data.get("localidade", ""),
        "estado": data.get("uf", "")
    }

def busca_logradouro(logradouro, cidade, estado):
    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{logradouro}/json/"
    response = request.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Erro na requisição: {response.status_code}")
    data = response.json()
    if isinstance(data, dict) and "erro" in data:
        raise ValueError("Logradouro não encontrado.")
    resultados = []
    resultados.extend(
        {
            "cep": item.get("cep", ""),
            "logradouro": item.get("logradouro", ""),
            "bairro": item.get("bairro", ""),
            "cidade": item.get("localidade", ""),
            "estado": item.get("uf", ""),
        }
        for item in data
    )
    return resultados