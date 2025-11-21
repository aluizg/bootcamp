import os

def get_api_key():
    try:
        return os.getenv("GoogleMapKey")
    except KeyError:
        raise EnvironmentError("A variável de ambiente 'GoogleMapKey' não está definida.")