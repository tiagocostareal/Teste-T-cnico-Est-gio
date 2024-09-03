def inverter_string(s):
    # Inicializar uma string vazia para armazenar o resultado
    resultado = ""
    
    # Iterar sobre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

def main():
    # Solicitar ao usuário para informar uma string
    entrada = input("Informe a string a ser invertida: ")
    
    # Inverter a string
    string_invertida = inverter_string(entrada)
    
    # Exibir a string invertida
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
