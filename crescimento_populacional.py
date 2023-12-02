# Função para calcular o crescimento populacional com base no primeiro princípio de indução
def crescimento_populacional(geracao_inicial, taxa_reproducao, numero_geracoes):
    populacao_atual = geracao_inicial

    print(f"Geração 0: {populacao_atual} indivíduos")

    # Aplicação do primeiro princípio de indução matemática
    for geracao in range(1, numero_geracoes + 1):
        # Cada geração subsequente é um múltiplo da geração anterior
        populacao_atual *= taxa_reproducao

        print(f"Geração {geracao}: {populacao_atual} indivíduos")

# Configuração inicial
geracao_inicial = 1  # Número de indivíduos na geração inicial
taxa_reproducao = 2  # Taxa de reprodução (cada geração é o dobro da anterior)
numero_geracoes = 5  # Número total de gerações

# Chamada da função para simular o crescimento populacional
crescimento_populacional(geracao_inicial, taxa_reproducao, numero_geracoes)