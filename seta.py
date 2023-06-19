def start_game(parent_window):
    from math import sin, cos, radians
    from tkinter import Toplevel, Canvas, Button, Label
    from PIL import ImageTk, Image
    from tkinter import LAST, NW

    # Lista de eventos do jogo
    events = [
        {
            "dialogue": "Felipe agora está treinando. Ele vai cruzar no treino.",
            "objective": "Ajude Felipe a cruzar a bola com sucesso.",
            "minigame": "crossing",
            "points": 10
        },
        {
            "dialogue": "Felipe agora está jogando uma partida. Ele precisa marcar um gol.",
            "objective": "Ajude Felipe a marcar um gol.",
            "minigame": "shooting",
            "points": 20
        }
    ]

    # Índice do evento atual
    current_event = 0

    # Pontuação do personagem
    score = 0
    
    def start_minigame(minigame):
        # Cria uma nova janela para o mini-jogo
        minigame_window = Toplevel(parent_window)
        canvas = Canvas(minigame_window, width=300, height=200)
        canvas.pack()
        
        # Desenha a linha da seta em movimento com largura aumentada
        arrow = canvas.create_line(150, 100, 250, 100, arrow=LAST, width=3)

        # Desenha a linha da seta fantasma com largura aumentada
        ghost_arrow = canvas.create_line(150, 100, 150, 0, arrow=LAST, fill="gray", width=3)

        # Variáveis para controlar o ângulo e a velocidade angular da seta
        angle = -90
        omega = 5

        def update_arrow():
            nonlocal angle, omega
            # Atualiza o ângulo da seta
            angle += omega

            # Verifica se o ângulo está dentro do intervalo desejado
            if angle < -180 or angle > 0:
                # Inverte a direção da seta
                omega = -omega
                angle += omega

            # Calcula a posição da ponta da seta usando trigonometria
            x = 150 + 100 * cos(radians(angle))
            y = 100 + 100 * sin(radians(angle))

            # Atualiza a posição da seta
            canvas.coords(arrow, 150, 100, x, y)

            # Agenda a próxima atualização
            minigame_window.after(50, update_arrow)

        def on_button_click():
            nonlocal omega
            # Para a seta em movimento
            omega = 0

            # Adiciona um atraso de 2 segundos antes de exibir o resultado
            minigame_window.after(2000, show_result)

        def show_result():
            # Fecha a janela do mini-jogo
            minigame_window.destroy()

            # Calcula a chance de sucesso com base na posição da seta
            success_chance = max(0, 1 - abs(angle) / 180)

            # Verifica se o jogador teve sucesso no mini-jogo
            if success_chance > 0.5:
                result_text = f"Success! {events[current_event]['objective']}"
                add_points(events[current_event]["points"])
                advance_event()
            else:
                result_text = f"Failure! {events[current_event]['objective']}"

            # Cria um label para exibir o resultado
            result_label = Label(parent_window, text=result_text)
            result_label.pack()

        # Adiciona um botão para parar a seta em movimento
        button = Button(minigame_window, text="Stop", command=on_button_click)
        button.pack()

        # Inicia o loop de atualização
        update_arrow()

    def add_points(points):
        nonlocal score
        # Adiciona pontos à pontuação do personagem
        score += points

        # Atualiza o label de pontuação na interface do jogo
        score_label["text"] = f"Score: {score}"

    def advance_event():
        nonlocal current_event

        # Avança para o próximo evento
        current_event += 1
        if current_event < len(events):
            # Mostra o diálogo do próximo evento
            dialogue_label["text"] = events[current_event]["dialogue"]
        else:
            # Fim do jogo
            dialogue_label["text"] = "Fim do jogo!"

    # Cria a janela principal do jogo
    root = Toplevel(parent_window)
    canvas = Canvas(root, width=300, height=200)
    canvas.pack()

    # Carrega a imagem de grama
    grass_image = Image.open("grama.jpg")
    # Redimensiona a imagem para o tamanho do canvas
    grass_image = grass_image.resize((300, 200), Image.ANTIALIAS)
    grass_photo = ImageTk.PhotoImage(grass_image)
    # Desenha a imagem de grama no fundo do canvas
    canvas.create_image(0, 0, image=grass_photo, anchor=NW)

    # Adiciona um label para mostrar o diálogo do evento atual
    dialogue_label = Label(root, text=events[current_event]["dialogue"], wraplength=300)
    dialogue_label.pack()

    # Adiciona um label para mostrar a pontuação do personagem
    score_label = Label(root, text=f"Score: {score}")
    score_label.pack()

    # Adiciona um botão para iniciar o mini-jogo
    button = Button(root, text="Start minigame", command=lambda: start_minigame(events[current_event]["minigame"]))
    button.pack()

# Example usage:
# from tkinter import Tk
# root = Tk()
# start_game(root)
# root.mainloop()
