# Lucas Gusmão Valduga

# Repositório https://github.com/TheValduga/SC_Clouds_Challenge

'''
    Esta implementação recursiva do algoritmo de Fibonacci possui complexidade de O(2^n), 
o que significa que o tempo de execução cresce exponencialmente quando a posição desejada da sequencia aumenta. 
    Isso ocorre porque a função FibonacciRecursivo faz chamadas recursivas para calcular os dois termos 
anteriores da sequência, resultando em muitas chamadas redundantes para os mesmos valores.
    Chamadas para calcular termos acima da posição 40 aproximadamente 
ja começam a levar tempo significativo para serem computadas
'''

# Essa primeira função só valida o input, se colocasse na recursiva iria validar n a cada chamada
def Fibonacci(n: str) -> str | int: 
    if (not n.isdigit()):
        return "Número de termos inválido. Por favor, informe um número inteiro positivo."
    return FibonacciRecursivo(int(n))
      
def FibonacciRecursivo(n: int) -> int:
    if n <= 1: # Determina onde a recursão deve parar, ou seja, quando n for 0 ou 1, retorna n, pois 0 e 1 sao os primeiros dois termos da sequencia de Fibonacci
        return n
    # A função chama a si mesma para calcular os dois termos anteriores da sequência e soma os resultados
    return FibonacciRecursivo(n - 1) + FibonacciRecursivo(n - 2) 

if __name__ == "__main__":
    n = input("Informe o número do termo da sequência de Fibonacci que deseja calcular: ")
    print(Fibonacci(n))
    