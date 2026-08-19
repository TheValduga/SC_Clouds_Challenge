
# Lucas Gusmão Valduga

# Implementado algoritmo do Crivo de Eratóstenes para encontrar todos os números primos menores ou iguais a n
# Referências: https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes , https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html

# Repositório https://github.com/TheValduga/SC_Clouds_Challenge

from math import isqrt

def NumerosPrimosIterativo(n: str) -> str | list[int]:
    # Valida o input
    if (not n.isdigit() or int(n) < 2):
        return "Número inválido. Por favor, informe um número inteiro positivo maior ou igual a 2."
    
    N = int(n)
    primos = [] # Lista para armazenar os números primos encontrados
    # Lista boolean para marcar números primos (True) e não primos (False)
    boolList = [True] * (N - 1) # Essa lista tem tamanho n-1 pois nao vamos verificar o 0 e o 1, que nao sao primos

    for num in range(2, isqrt(N) + 1): # O range vai até raiz de N arredondada para baixo pois assim determina o algoritmo do Crivo de Eratóstenes
        if boolList[num - 2]: # A posição é -2 pois a lista começa no 0 e o primeiro número primo é 2
            for multiple in range(num**2, N + 1, num): # Percorre os múltiplos do primo encontrado
                boolList[multiple - 2] = False # Marca os múltiplos do primo como não primos (False)

    for i in range(N - 1): # Percorre a lista de booleanos para coletar os números primos
        if boolList[i]: # Se o número for primo (True), adiciona à lista de primos
            primos.append(i + 2) # Adiciona o número primo à lista, ajustando o índice para corresponder ao número real
    return primos

if __name__ == "__main__":
    n = input("Informe o número que deseja listar primos menores ou igual: ")
    print(NumerosPrimosIterativo(n))