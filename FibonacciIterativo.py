# Lucas Gusmão Valduga

def FibonacciIterativo(n: str)-> str | int:
    if (not n.isdigit()):
        return "Número de termos inválido. Por favor, informe um número inteiro positivo."      
    a, b = 0, 1
    for _ in range(int(n)):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    n = input("Informe o número do termo da sequência de Fibonacci que deseja calcular: ")
    print(FibonacciIterativo(n))