import json

def calcular_faturamento(file_path):
    try:
        # Ler o arquivo JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return

    # Extrair a lista de faturamento
    faturamento = [item['valor'] for item in data.get('faturamento', []) if item.get('valor', 0) > 0]
    
    if not faturamento:
        print("Não há dados de faturamento para processar.")
        return

    # Calcular o menor e o maior valor de faturamento
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    
    # Calcular a média mensal
    media_mensal = sum(faturamento) / len(faturamento)
    
    # Contar o número de dias com faturamento superior à média
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    # Imprimir os resultados
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Função principal
if __name__ == "__main__":
    # Caminho para o arquivo JSON
    file_path = 'dados.json'  
    calcular_faturamento(file_path)
