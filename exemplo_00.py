# Bibliotecas
from typing import List
import random

#lista  para usar nas function para testar
valores_aleatorios = [random.uniform(0, 20) for _ in range(10)]

df = [11.66, 5.01, 5.35, 17.54, 4.78, 1.80, 4.78, 12.51, 1.09, 4.88]

# function de somar
def soma(valor_1:float , valor_2:float ) -> float:
    '''
    uma funcao simples de soma de valores tipo float que retonar float
    '''
    resultado_soma = valor_1 + valor_2
    return resultado_soma

def cumprimentar(nome:str , mensagem="Ola"):
    '''
    Função de colocar nome e enviar uma mensagem, caso querira trocar a mensagem use o argumento mensagem= e seu texto
    '''
    nome = nome.title()
    resultado_mensagem = print(f"{mensagem}, {nome} espero que tenha dado certo sua função")

    return resultado_mensagem

# Calcular Média de Valores em uma Lista



def calcular_media(valores: List[float]) -> float:
    calculo = sum(valores) / len(valores)

    return calculo

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            valor = round(valor,2)
            resultado.append(valor) # acrescentando o valor na lista
            
    resultado.sort() # ordenando a lista de forma crescente
    return resultado

def contar_valores_unicos(lista: List[int]) ->int:
    return len(set(lista))


def celsius_to_fahrenheit(temperatura_celsius: List[float]) -> float:
    calculo_temp = [ round((9/5) * temp + 32,2) for temp in temperatura_celsius]
    return calculo_temp

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    resultado = round(variancia ** 0.5,2)
    return resultado



