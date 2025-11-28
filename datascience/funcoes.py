import os
import pandas as pd

def load_data(dir_name, file_name, file_type='csv'):
    # Obtem caminho correto do arquivo independente do sistema operacional
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, dir_name, file_name)

    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    else:
        raise ValueError("Arquivo nao suportado'.")

def save_graph(fig, dir_name, file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, dir_name)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, file_name)
    fig.savefig(file_path)