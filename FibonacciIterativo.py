# Lucas Gusmão Valduga

# Repositório https://github.com/TheValduga/SC_Clouds_Challenge

def FibonacciIterativo(n: str)-> str | int:
    # Valida o input
    if (not n.isdigit()):
        return "Número de termos inválido. Por favor, informe um número inteiro positivo."      
    a, b = 0, 1 # Dois primeiros termos da sequência de Fibonacci
    for _ in range(int(n)):
        # Calcula sempre um termo a frente do atual, assim a variável 'a' sempre vai armazenar o termo atual da sequência
        a, b = b, a + b 
    return a 

if __name__ == "__main__":
    n = input("Informe o número do termo da sequência de Fibonacci que deseja calcular: ")
    print(FibonacciIterativo(n))