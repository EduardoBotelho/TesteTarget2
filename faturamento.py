import json

# Supondo que temos um arquivo faturamento.json
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Menor e maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Cálculo da média
media_mensal = sum(faturamento) / len(faturamento)

# Número de dias com faturamento acima da média
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
