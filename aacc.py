import random

# Função para simular a participação em atividades extracurriculares para a disciplina da Fatec
def participacao_atividades_extra(periodo, beneficio_base):
    semanas_participadas = 0
    beneficio_total = 0

    # Aplicação do primeiro princípio de indução matemática
    for semana in range(1, periodo + 1):
        # Simulação: O estudante decide se participa na semana
        participou_semana = random.choice([True, False])

        if participou_semana:
            semanas_participadas += 1
            beneficio_total += beneficio_base

            print(f" Semana {semana}: Participação! Benefício acumulado: {beneficio_total}")
        else:
            print(f" Semana {semana}: Não participou. Benefício acumulado: {beneficio_total}")

    print(f"\nTotal de semanas participadas: {semanas_participadas}")
    print(f"Benefício total acumulado: {beneficio_total}")

# Configuração inicial
periodo = 8  # Número total de semanas para simulação
beneficio_base = 3  # Benefício associado à participação em atividades extracurriculares

# Chamada da função para simular a participação em atividades extracurriculares
participacao_atividades_extra(periodo, beneficio_base)