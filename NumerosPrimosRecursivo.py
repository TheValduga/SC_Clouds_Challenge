# Lucas Gusmão Valduga

# Implementado algoritmo do Crivo de Eratóstenes para encontrar todos os números primos menores ou iguais a n
# Adaptado algoritmo do Crivo de Eratóstenes para implementação recursiva
# Referências: https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes , https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html

# Repositório https://github.com/TheValduga/SC_Clouds_Challenge

from math import isqrt

def ConvertePrimos(boolList: list[bool], primos: list[int], index: int) -> list[int]:
    # Se o índice atual for igual ao tamanho da lista booleana, significa que todos os números foram verificados e a lista de primos está completa
    if index == len(boolList):
        return primos

    # Se o número correspondente ao índice atual for primo (True), adiciona à lista de primos
    if boolList[index]:
        primos.append(index + 2) # Primo é o index + 2 pois o primeiro número primo é 2 e a lista booleana começa no índice 0

    return ConvertePrimos(boolList, primos, index + 1)

def BuscaMultiplos(boolList: list[bool], primoAtual: int, multiplo: int, N: int,) -> list[bool]:
    # Condição de parada da recursão, quando o múltiplo atual for maior que o N desejado, termina a busca do múltiplos do primo atual
    if multiplo > N:
        return boolList

    else:
        # Marca o múltiplo do primo como não primo (False)
        boolList[ multiplo - 2] = False 
        # Chama a função recursivamente para o próximo múltiplo do primo atual, que será marcado como não primo
        return BuscaMultiplos(boolList, primoAtual, multiplo + primoAtual, N)
    
def CrivoDeEratostenes(N: int, boolList: list[bool], num: int) -> list[bool]:
    # Condição de parada da recursão, quando o número atual for maior que a raiz quadrada de N arredondada para baixo, confrome define o Crivo de Eratóstenes
    if num > isqrt(N):
        # Se chegar na condição de parada a lista booleana de primos esta completa 
        return boolList 

    # Se o número atual for primo, chama a função para marcar os múltiplos do primo como não primos
    elif boolList[num - 2]: 
        BuscaMultiplos(boolList, num, num**2, N)

    # Chama a função recursivamente para o próximo número, que será verificado se é primo ou não
    return CrivoDeEratostenes(N, boolList, num + 1) 

def NumerosPrimosRecursivo(n: str) -> str | list[int]:
    # Valida o input
    if not n.isdigit() or int(n) < 2:
        return "Número inválido. Por favor, informe um número inteiro positivo maior ou igual a 2."

    N = int(n)

    # Lista boolean para marcar números primos (True) e não primos (False)
    boolList = [True] * (N - 1) # Essa lista tem tamanho n-1 pois nao vamos verificar o 0 e o 1, que nao sao primos
    primos = [] # Lista para armazenar os números primos encontrados

    # Chama o crivo que retornará a lista de primos booleana, e em seguida chama a função que converterá a lista booleana na lista de primos inteiros
    return ConvertePrimos(CrivoDeEratostenes(N, boolList, 2), primos, 0)

if __name__ == "__main__":
    n = input("Informe o número que deseja listar primos menores ou igual: ")
    print(NumerosPrimosRecursivo(n))
