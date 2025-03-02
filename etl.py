import csv
import pandas as pd



def ler_csv(nome_arquivo:str) -> list[dict]:
    """
    Funcao que le arquivo e retorna uma lista 
    de dicionarios
    """
    lista = []
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
        lista: list[dict]    
        return lista





def filtrando_dataframe(nome_arquivo: str, col: str, filter_condition=True, operador: str = "=="):
    df = pd.read_csv(nome_arquivo, encoding="utf-8")
    df = df.query(f"{col} {operador} {filter_condition}")
    return df




