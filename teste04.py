def calcular_percentuais(faturamento_por_estado):
    # Calcular o faturamento total
    total_faturamento = sum(faturamento_por_estado.values())
    
    # Calcular o percentual de representação de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_por_estado.items()}
    
    return percentuais

def main():
    # Faturamento por estado
    faturamento_por_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    # Calcular percentuais
    percentuais = calcular_percentuais(faturamento_por_estado)
    
    # Exibir resultados
    print("Percentual de representação de cada estado no faturamento total:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
