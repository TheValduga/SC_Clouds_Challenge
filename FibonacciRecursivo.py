# Lucas Gusmão Valduga

'''
    Esta implementação recursiva do algoritmo de Fibonacci possui complexidade de O(2^n), 
o que significa que o tempo de execução cresce exponencialmente quando a posição desejada da sequencia aumenta. 
    Isso ocorre porque a função FibonacciRecursivo faz chamadas recursivas para calcular os dois termos 
anteriores da sequência, resultando em muitas chamadas redundantes para os mesmos valores.
    Chamadas para calcular termos acima da posição 40 aproximadamente 
ja começam a levar tempo significativo para serem computadas
'''

def Fibonacci(n: str) -> str | int:
    if (not n.isdigit()):
        return "Número de termos inválido. Por favor, informe um número inteiro positivo."
    return FibonacciRecursivo(int(n))
      
def FibonacciRecursivo(n: int) -> int:
    if n <= 1:
        return n
    return FibonacciRecursivo(n - 1) + FibonacciRecursivo(n - 2)

if __name__ == "__main__":
    n = input("Informe o número do termo da sequência de Fibonacci que deseja calcular: ")
    print(Fibonacci(n))
    