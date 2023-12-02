import turtle

# Função para desenhar um quadrado colorido
def desenhar_quadrado(turtle, tamanho, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(tamanho)
        turtle.left(90)
    turtle.end_fill()

# Função para adicionar um quadrado à obra de arte e aplicar a indução
def adicionar_quadrado(turtle, tamanho, cor):
    # Mantém ou modifica o padrão inicial
    desenhar_quadrado(turtle, tamanho, cor)
    turtle.forward(tamanho)
    turtle.left(30)  # Regra: girar 30 graus à esquerda após cada adição

# Configuração inicial da tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(2)  # Ajuste a velocidade conforme necessário

# Padrão inicial: Quadrado vermelho
desenhar_quadrado(tartaruga, 50, "red")

# Aplicação do primeiro princípio de indução matemática:
# A cada iteração, adicionamos um quadrado mantendo ou modificando o padrão inicial.

# Adição 1: Quadrado azul
adicionar_quadrado(tartaruga, 50, "blue")

# Adição 2: Quadrado verde
adicionar_quadrado(tartaruga, 50, "green")

# Adição 3: Quadrado amarelo
adicionar_quadrado(tartaruga, 50, "yellow")

# Adição 4: Quadrado roxo
adicionar_quadrado(tartaruga, 50, "purple")

# Adição 5: Quadrado laranja
adicionar_quadrado(tartaruga, 50, "orange")

# Mantenha a janela aberta
turtle.mainloop()
