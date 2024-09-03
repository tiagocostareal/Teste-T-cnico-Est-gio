def pertence_a_fibonacci(n):
    if n < 0:
        return False

    # Inicializar os dois primeiros números da sequência
    a, b = 0, 1
    
    # Verificar se o número é 0 ou 1
    if n == a or n == b:
        return True

    # Gerar números da sequência de Fibonacci
    while b < n:
        a, b = b, a + b
    
    # Verificar se o número está na sequência
    return b == n

# Função principal para entrada e verificação
def main():
    try:
        numero = int(input("Informe um número: "))
        if pertence_a_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, informe um número inteiro válido.")

if __name__ == "__main__":
    main()
