import random
import mysql.connector
from jogo_individual import run_game

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="brasfoot"
)

def get_team_points(conn, team_name):
    # Create a cursor object
    cursor = conn.cursor()

    # Define the query
    query = "SELECT pontos_de_forca FROM time WHERE nome = %s"

    # Execute the query
    cursor.execute(query, (team_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor to discard any unread results
    for result in cursor:
        pass
    cursor.close()

    # Check if a result was found
    if result:
        # Return the value of the pontos column
        return result[0]
    else:
        # No result found
        return None

def simular_jogo(conn, time_casa, time_visitante):
    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Seleciona os pontos de força dos times
    cursor.execute("SELECT pontos_de_forca FROM time WHERE nome = %s", (time_casa,))
    pontos_time_casa = cursor.fetchone()[0]
    cursor.execute("SELECT pontos_de_forca FROM time WHERE nome = %s", (time_visitante,))
    pontos_time_visitante = cursor.fetchone()[0]

    # Fecha o cursor para descartar quaisquer resultados não lidos
    for result in cursor:
        pass
    cursor.close()

    # Adiciona um fator de aleatoriedade aos pontos de força dos times
    fator_aleatorio = random.uniform(0.8, 1.2)
    pontos_time_casa *= fator_aleatorio
    pontos_time_visitante *= fator_aleatorio

    # Definir o placar do jogo
    placar = [0, 0]  # gols do time e do adversário

    # Simular o jogo em 10 iterações
    for i in range(10):
        # Calcular a probabilidade de cada time marcar um gol
        probabilidade_time_casa = (pontos_time_casa / (pontos_time_casa + pontos_time_visitante)) * 0.3
        probabilidade_time_visitante = (pontos_time_visitante / (pontos_time_casa + pontos_time_visitante)) * 0.3
        
        # Gerar um número aleatório usando uma distribuição normal
        resultado = random.gauss(0.5, 0.2)

        # Comparar o resultado com as probabilidades
        if resultado <= probabilidade_time_casa:
            # Se o resultado for menor ou igual à probabilidade do time da casa, ele marca um gol
            placar[0] += 1
        elif resultado <= probabilidade_time_casa + probabilidade_time_visitante:
            # Se o resultado for menor ou igual à soma das probabilidades do time da casa e do time visitante, o time visitante marca um gol
            placar[1] += 1

        # Simular um evento aleatório de pênalti
        if random.random() <= 0.05:
            if random.random() <= 0.5:
                # Pênalti para o time da casa
                placar[0] += 1
            else:
                # Pênalti para o time visitante
                placar[1] += 1

        # Simular um evento aleatório de cartão vermelho
        if random.random() <= 0.03:
            if random.random() <= 0.5:
                # Cartão vermelho para o time da casa
                pontos_time_casa *= 0.8
            else:
                # Cartão vermelho para o time visitante
                pontos_time_visitante *= 0.8

    # Atualizar os valores na tabela time

    cursor = conn.cursor()

    if placar[0] > placar[1]:
        # Vitória do time da casa
        cursor.execute("UPDATE time SET vitorias = vitorias + 1 WHERE nome = %s", (time_casa,))
        cursor.execute("UPDATE time SET derrotas = derrotas + 1 WHERE nome = %s", (time_visitante,))
    elif placar[0] < placar[1]:
        # Vitória do time visitante
        cursor.execute("UPDATE time SET vitorias = vitorias + 1 WHERE nome = %s", (time_visitante,))
        cursor.execute("UPDATE time SET derrotas = derrotas + 1 WHERE nome = %s", (time_casa,))
    else:
        # Empate
        cursor.execute("UPDATE time SET empates = empates + 1 WHERE nome = %s", (time_casa,))
        cursor.execute("UPDATE time SET empates = empates + 1 WHERE nome = %s", (time_visitante,))

    # Atualizar os gols marcados e sofridos
    cursor.execute("UPDATE time SET gols_marcados = gols_marcados + %s, gols_sofridos = gols_sofridos + %s WHERE nome = %s", (placar[0], placar[1], time_casa))
    cursor.execute("UPDATE time SET gols_marcados = gols_marcados + %s, gols_sofridos = gols_sofridos + %s WHERE nome = %s", (placar[1], placar[0], time_visitante))

    # Salva as alterações no banco de dados
    conn.commit()
    
    # Fecha o cursor para descartar quaisquer resultados não lidos
    for result in cursor:
        pass
    cursor.close()

    # Retornar o placar final
    return placar

def simular_rodada(conn, rodada, time_especifico=None):
    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Seleciona os jogos da rodada especificada
    cursor.execute("SELECT time_casa, time_visitante FROM rodadas_brasileirao WHERE rodada = %s", (rodada,))
    jogoss = cursor.fetchall()

    # Fecha o cursor para descartar quaisquer resultados não lidos
    for result in cursor:
        pass

    cursor.close()

    # Simula cada jogo da rodada
    #print(jogos)
    jogos = list(set(jogoss))
    print(jogos) # [1, 2, 3, 4, 5]

    for jogo in jogos:
        time_casa, time_visitante = jogo
        if time_especifico is not None and (time_casa == time_especifico or time_visitante == time_especifico):
            # Pula a simulação desse jogo se um dos times é o time específico
            continue
        placar = simular_jogo(conn, time_casa, time_visitante)
        print(f"{time_casa} {placar[0]} x {placar[1]} {time_visitante}")

# Seleciona o jogo do Palmeiras na rodada 1
cursor = conn.cursor()
cursor.execute("SELECT time_casa, time_visitante FROM rodadas_brasileirao WHERE rodada = 1 AND (time_casa = 'Palmeiras' OR time_visitante = 'Palmeiras')")
jogo_palmeiras = cursor.fetchone()
time_casa, time_visitante = jogo_palmeiras

# Fecha o cursor para descartar quaisquer resultados não lidos
for result in cursor:
    pass

cursor.close()

'''# Simula apenas o jogo do Palmeiras na rodada 1
placar = simular_jogo(conn, time_casa, time_visitante)

print(f"{time_casa} {placar[0]} x {placar[1]} {time_visitante}")'''

# Get the points for a team
team_name = time_casa
pontos_time_casa = get_team_points(conn, team_name)

team_name = time_visitante
pontos_time_visitante= get_team_points(conn, team_name)

placar_time_casa, placar_time_visitante = run_game(time_casa, time_visitante, pontos_time_casa, pontos_time_visitante)

cursor = conn.cursor()

if placar_time_casa > placar_time_visitante:
    # Vitória do time da casa
    cursor.execute("UPDATE time SET vitorias = vitorias + 1 WHERE nome = %s", (time_casa,))
    cursor.execute("UPDATE time SET derrotas = derrotas + 1 WHERE nome = %s", (time_visitante,))
elif placar_time_casa < placar_time_visitante:
    # Vitória do time visitante
    cursor.execute("UPDATE time SET vitorias = vitorias + 1 WHERE nome = %s", (time_visitante,))
    cursor.execute("UPDATE time SET derrotas = derrotas + 1 WHERE nome = %s", (time_casa,))
else:
    # Empate
    cursor.execute("UPDATE time SET empates = empates + 1 WHERE nome = %s", (time_casa,))
    cursor.execute("UPDATE time SET empates = empates + 1 WHERE nome = %s", (time_visitante,))

# Atualizar os gols marcados e sofridos
cursor.execute("UPDATE time SET gols_marcados = gols_marcados + %s, gols_sofridos = gols_sofridos + %s WHERE nome = %s", (placar_time_casa, placar_time_visitante, time_casa))
cursor.execute("UPDATE time SET gols_marcados = gols_marcados + %s, gols_sofridos = gols_sofridos + %s WHERE nome = %s", (placar_time_visitante, placar_time_casa, time_visitante))

# Salva as alterações no banco de dados
conn.commit()

# Fecha o cursor para descartar quaisquer resultados não lidos
for result in cursor:
    pass
cursor.close()
# Simula a rodada 1, exceto o jogo do Palmeiras
simular_rodada(conn, 1, "Palmeiras")

# Fecha a conexão com o banco de dados
for result in cursor:
    pass

conn.close()
