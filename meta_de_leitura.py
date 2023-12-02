import random

# Função para simular o cumprimento de metas diárias de leitura
def cumprimento_metas_leitura(meta_diaria, numero_dias, beneficio_base):
    dias_cumpridos = 0
    beneficio_total = 0

    # Aplicação do primeiro princípio de indução matemática
    for dia in range(1, numero_dias + 1):
        # Simulação: O estudante decide se cumpre a meta diária
        cumpriu_meta = random.choice([True, False])

        if cumpriu_meta:
            dias_cumpridos += 1
            beneficio_total += beneficio_base

            print(f" Dia {dia}: Meta cumprida! Benefício acumulado: {beneficio_total}")
        else:
            print(f" Dia {dia}: Meta não cumprida. Benefício acumulado: {beneficio_total}")

    print(f"\nTotal de dias com a meta cumprida: {dias_cumpridos}")
    print(f"Benefício total acumulado: {beneficio_total}")

# Configuração inicial
meta_diaria = 1  # Número de capítulos, páginas ou tempo de leitura diária
numero_dias = 10  # Número total de dias para simulação
beneficio_base = 2  # Benefício associado ao cumprimento da meta diária

# Chamada da função para simular o cumprimento de metas de leitura
cumprimento_metas_leitura(meta_diaria, numero_dias, beneficio_base)