import math
import random
import random
import tkinter as tk
import time
from variaveis_time import consultar_time, consultar_ultima_rodada_simulada
from tkinter import Tk
from seta import start_game
import mysql.connector


'''root = Tk()
start_game(root)
root.mainloop()'''


id1 = ''
media_gols_tomados_time_2 = ''
media_gols_tomados_time_1 = ''
resultados = consultar_time("palmeiras")
for row in resultados:
    id1 = row[0]
    nome1 = row[1]
    pontos_de_classificacao1 = row[2]
    pontos_de_forca1 = row[3]
    vitorias1 = row[4]
    derrotas1 = row[5]
    empates1 = row[6]
    gols_marcados1 = row[7]
    gols_sofridos1 = row[8]
    pontos_de_ataque1 = row[9]
    pontos_de_defesa1 = row[10]

resultados = consultar_time("flamengo")
for row in resultados:
    id2 = row[0]
    nome2 = row[1]
    pontos_de_classificacao2 = row[2]
    pontos_de_forca2 = row[3]
    vitorias2 = row[4]
    derrotas2 = row[5]
    empates2 = row[6]
    gols_marcados2 = row[7]
    gols_sofridos2 = row[8]
    pontos_de_ataque2 = row[9]
    pontos_de_defesa2 = row[10]
global forca_geral_time1_adjusted
global forca_geral_time2_adjusted
qual_rodada_estamos = consultar_ultima_rodada_simulada()
media_gols_tomados_time_1 = int(gols_sofridos1) / int(qual_rodada_estamos)
media_gols_feitos_time_1 = int(gols_marcados1) / int(qual_rodada_estamos)
#vantagem_time_1 = (int(media_gols_feitos_time_1) + int(media_gols_tomados_time_2)) * 15
vantagem_time_1 = 1
#print("vantagem_time_1: "+str(vantagem_time_1))
forca_geral_time1 = (int(pontos_de_ataque1) + int(pontos_de_defesa1)) / 2
forca_geral_time2 = (int(pontos_de_ataque1) + int(pontos_de_defesa1)) / 2
diferenca1 = forca_geral_time1 - forca_geral_time2
forca_geral_time1_adjusted = forca_geral_time1 + vantagem_time_1 + diferenca1


media_gols_tomados_time_2 = int(gols_sofridos2) / int(qual_rodada_estamos)
media_gols_feitos_time_2 = int(gols_marcados2) / int(qual_rodada_estamos)
#vantagem_time_2 = (int(media_gols_feitos_time_2) + int(media_gols_tomados_time_1)) * 15
vantagem_time_2 = 1
#print("vantagem_time_2: "+str(vantagem_time_2))
forca_geral_time1 = (int(pontos_de_ataque1) + int(pontos_de_defesa1)) / 2
forca_geral_time2 = (int(pontos_de_ataque1) + int(pontos_de_defesa1)) / 2
diferenca2 = forca_geral_time2 - forca_geral_time1
forca_geral_time2_adjusted = forca_geral_time2 + vantagem_time_2 + diferenca2
forca_geral_time1_adjusted = forca_geral_time1 + vantagem_time_1 + diferenca1

qual_rodada_estamos = consultar_ultima_rodada_simulada()
    
media_gols_tomados_time_1 = gols_sofridos1 / qual_rodada_estamos
media_gols_tomados_time_2 = gols_sofridos2 / qual_rodada_estamos

media_gols_feitos_time_1 = gols_marcados1 / qual_rodada_estamos
media_gols_feitos_time_2 = gols_marcados2 / qual_rodada_estamos

forca_geral_time1 = ( pontos_de_ataque1 + pontos_de_defesa1 ) / 2
forca_geral_time2 = ( pontos_de_ataque1 + pontos_de_defesa1 ) / 2
#vantagem_time_1 = (media_gols_feitos_time_1 + media_gols_tomados_time_2) * 15
#vantagem_time_2 = (media_gols_feitos_time_2 + media_gols_tomados_time_1) * 15
vantagem_time_1 = 1
vantagem_time_2 = 2




diferenca1 = forca_geral_time1 - forca_geral_time2
diferenca2 = forca_geral_time2 - forca_geral_time1



forca_geral_time1_adjusted = forca_geral_time1 + vantagem_time_1 + diferenca1
forca_geral_time2_adjusted = forca_geral_time2  + vantagem_time_2 + diferenca2

counter = 0



def lance_de_perigo_ou_nao(nome_do_time):

    

    numero_aleatorio = random.random()

    
    
    

def duelo(nome1, pontos_de_classificacao1, pontos_de_forca1, vitorias1, derrotas1, empates1, 
    gols_marcados1, gols_sofridos1, pontos_de_ataque1, pontos_de_defesa1, nome2, pontos_de_classificacao2, 
    pontos_de_forca2, vitorias2, derrotas2, empates2, gols_marcados2, gols_sofridos2, pontos_de_ataque2, pontos_de_defesa2):
    
    def probability_of_victory(forca_geral_time1, forca_geral_time2):
        return 1 / (1 + math.pow(10, (forca_geral_time2 - forca_geral_time1) / 400))
    
    
    team_1_probability = probability_of_victory(forca_geral_time1_adjusted, forca_geral_time2_adjusted)
    team_2_probability = probability_of_victory(forca_geral_time2_adjusted, forca_geral_time1_adjusted)

    #print("vantagem_time_1: "+str(vantagem_time_1))
    #print("vantagem_time_2: "+str(vantagem_time_2))

    #print("Probabilidade de vitória do Time A:", round(team_1_probability * 100), "%")
    #print("Probabilidade de vitória do Time B:", round(team_2_probability * 100), "%")

    probability_of_outcome_1 = team_1_probability
    probability_of_outcome_2 = team_2_probability
    
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Check which outcome the random number corresponds to
    if random_number < probability_of_outcome_1:
        time_que_ganhou = nome1
        #print("time_que_ganhou: "+str(nome1))
    else:
        time_que_ganhou = nome2
        #print("time_que_ganhou: "+str(nome2))
    return time_que_ganhou

def run_game(nome1, pontos_de_classificacao1, pontos_de_forca1, vitorias1, derrotas1, empates1, 
    gols_marcados1, gols_sofridos1, pontos_de_ataque1, pontos_de_defesa1, nome2, pontos_de_classificacao2, 
    pontos_de_forca2, vitorias2, derrotas2, empates2, gols_marcados2, gols_sofridos2, pontos_de_ataque2, pontos_de_defesa2):
    

    start_time = time.time()

    # Definir a posse de bola do time
    posse = 60  # porcentagem
    global tempo
    # Definir o tempo de jogo
    tempo = 45  # minutos

    # Definir o placar do jogo
    placar = [0, 0]  # gols do time e do adversário

    # Criar a janela do Tkinter
    roott = tk.Tk()
    roott.title("Placar")

    # Criar o Listbox com uma largura e altura maiores
    eventos = tk.Listbox(roott, font=("Arial", 14), width=50, height=20)
    eventos.pack()

    # Criar os labels para mostrar o placar e o tempo restante
    label_time1 = tk.Label(roott, text=nome1 + ": " + str(placar[0]), font=("Arial", 24))
    label_time2 = tk.Label(roott, text=nome2 + ": " + str(placar[1]), font=("Arial", 24))
    label_tempo = tk.Label(roott, text="Tempo restante: " + str(tempo) + " minutos", font=("Arial", 18))

    # Posicionar os labels na janela
    label_time1.pack()
    label_time2.pack()
    label_tempo.pack()

    # Definir uma lista de nomes de jogadores para cada equipe
    players_time1 = ["Joao", "Pedro", "Lucas"]
    players_time2 = ["Dudu", "Carlos", "Rafael"]

    # Atualizar a janela
    roott.update()

    def adicionar_evento(evento):
        # Obter o tempo atual do jogo
        minutos = 1 - tempo

        # Adicionar o evento à lista
        eventos.insert(tk.END, f"{minutos}': {evento}")

        # Rolar a lista para baixo para mostrar o último evento
        eventos.yview(tk.END)

    def qual_time_tem_o_lance():
        # Escolher um número aleatório entre 0 e 1
        time_com_lance = duelo(nome1, pontos_de_classificacao1, pontos_de_forca1, vitorias1, derrotas1, empates1, gols_marcados1, gols_sofridos1, pontos_de_ataque1, pontos_de_defesa1, nome2, pontos_de_classificacao2, pontos_de_forca2, vitorias2, derrotas2, empates2, gols_marcados2, gols_sofridos2, pontos_de_ataque2, pontos_de_defesa2)
        print(time_com_lance)
        return time_com_lance

    def qual_tipo_de_lance(time_com_lance):
        tipo_de_lance = lance_de_perigo_ou_nao(time_com_lance)

        return tipo_de_lance
    
    def lance_de_perigo(time_com_lance):
        # Verificar se o time tem a posse de bola
        #print("lance_de_perigo + time_com_lance: "+str(time_com_lance))
        
        


        def probability_of_victory(forca_geral_time1, forca_geral_time2):
            return 1 / (1 + math.pow(10, (forca_geral_time2 - forca_geral_time1) / 400))
        team_1_probability = probability_of_victory(forca_geral_time1_adjusted, forca_geral_time2_adjusted)
        team_2_probability = probability_of_victory(forca_geral_time2_adjusted, forca_geral_time1_adjusted)

        #print("vantagem_time_1: "+str(vantagem_time_1))
        #print("vantagem_time_2: "+str(vantagem_time_2))

        #print("Probabilidade de vitória do Time A:", round(team_1_probability * 100), "%")
        #print("Probabilidade de vitória do Time B:", round(team_2_probability * 100), "%")

        probability_of_outcome_1 = team_1_probability
        probability_of_outcome_2 = team_2_probability
        #print("probability_of_outcome_1")
        #print(probability_of_outcome_1)
        # Generate a random number between 0 and 1
        random_number = random.randint(0, 10)
        # Check which outcome the random number corresponds to

        if time_com_lance == nome1:
            if random_number < probability_of_outcome_1:
                adicionar_evento(f"{nome1} tenta um ataque.")
                adicionar_evento(f"{nome1} tenta o gol.")
                placar[0] += 1
            else:
                adicionar_evento(f"{nome1} tenta um ataque.")
                adicionar_evento(f"{nome1} não deu em nada.")

                
        else:
            if random_number < probability_of_outcome_2:
                adicionar_evento(f"{nome2} tenta um ataque.")
                adicionar_evento(f"{nome2} tenta o gol.")
                placar[1] += 1
            else:
                adicionar_evento(f"{nome2} tenta um ataque.")
                adicionar_evento(f"{nome2} não deu em nada.")
    def lance_normal(time_com_lance):
        # Verificar se o time tem a posse de bola
        if time_com_lance == 'time1':
            adicionar_evento(f"{nome1} troca passes.")
        else:
            adicionar_evento(f"{nome2} troca passes.")

    def lance():
        global tempo
        global forca_geral_time1_adjusted
        global forca_geral_time2_adjusted
        global counter

        # Incrementar o contador
        counter += 1

        # Verificar se o contador atingiu 12
        if counter == 12:
            # Diminuir o tempo restante do jogo em 1 minuto
            tempo -= 1

            # Zerar o contador
            counter = 0

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="brasfoot"
        )

        cursor = conn.cursor()
        # Conectar ao banco de dados MySQL

        # Criar um cursor para executar consultas

        # Executar uma consulta SQL para recuperar os dados desejados
        query = "SELECT seta FROM game_performance"
        cursor.execute(query)

        # Recuperar o primeiro resultado da consulta
        first_line = cursor.fetchone()[0]

        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Print the first line
        print(first_line)

        if nome1 == 'Palmeiras':
            forca_geral_time1_adjusted += first_line
        elif nome2 == 'Palmeiras':
            forca_geral_time2_adjusted += first_line

    # Iterate over the
        # Atualizar o rótulo para o tempo restante
        
        minutos = tempo // 60

        # Atualizar o rótulo para o tempo restante
        label_tempo.config(text=f"Tempo: {tempo}")
        roott.update()

        # Escolher um número aleatório entre 0 e 1 para decidir se é um lance de perigo ou normal
        time_com_lance = qual_time_tem_o_lance()

        tipo_de_lance = qual_tipo_de_lance(time_com_lance)
        print(time_com_lance + str(tipo_de_lance))
        # Descobrir qual time tem o lance para ele

        #print("tipo_de_lance: "+str(tipo_de_lance))


            # Descobrir qual time tem o lance para ele
            
            #print("tipo_de_lance: "+str(tipo_de_lance))
 



        if tipo_de_lance == 0:
            lance_normal(time_com_lance)
        else:
            lance_de_perigo(time_com_lance)

        placar_str = [str(i) for i in placar]
        
        label_time1.config(text=nome1+ placar_str[0])
        label_time2.config(text=nome2+ placar_str[1])

        
        if tempo == 0:
            eventos.insert(tk.END, f"Jogo encerrado. Placar final: {placar_str[0]} x {placar_str[1]}")
            label_tempo.config(text="Fim de jogo")

        #print(tempo)
        if tempo > 0:
            roott.after(5000, lance)
        else:
            roott.destroy()

        
    roott.after(0, lance)
    
    roott.mainloop()

    return placar[0], placar[1]

run_game(nome1, pontos_de_classificacao1, pontos_de_forca1, vitorias1, derrotas1, empates1, 
    gols_marcados1, gols_sofridos1, pontos_de_ataque1, pontos_de_defesa1, nome2, pontos_de_classificacao2, 
    pontos_de_forca2, vitorias2, derrotas2, empates2, gols_marcados2, gols_sofridos2, pontos_de_ataque2, pontos_de_defesa2)