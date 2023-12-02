# Função para simular o crescimento de massa em uma receita de pão
def crescimento_massa(quantidade_inicial, tempo_crescimento, multiplicador, numero_iteracoes):
    massa_atual = quantidade_inicial

    print(f"Iteração 0: Massa inicial = {massa_atual} gramas")

    # Aplicação do primeiro princípio de indução matemática
    for iteracao in range(1, numero_iteracoes + 1):
        # Cada iteração simula o crescimento correto da massa
        massa_atual *= multiplicador

        print(f"Iteração {iteracao}: Massa atual = {massa_atual} gramas")

    print("Crescimento de massa concluído.")

# Configuração inicial
quantidade_inicial = 100  # Gramas de massa inicial
tempo_crescimento = 30  # Tempo de crescimento em minutos
multiplicador = 2  # Fator de crescimento (dobra a massa a cada iteração)
numero_iteracoes = 5  # Número total de iterações

# Chamada da função para simular o crescimento de massa
crescimento_massa(quantidade_inicial, tempo_crescimento, multiplicador, numero_iteracoes)