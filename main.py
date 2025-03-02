
from etl import *

path_arquivo = "produto.csv"

venda_itens = ler_csv(path_arquivo)

print(filtrando_dataframe(path_arquivo,"bebida"))

# mostrar camila