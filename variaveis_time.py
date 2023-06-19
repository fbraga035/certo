import mysql.connector

def consultar_time(nome_externo):
    # Conecte ao banco de dados
    cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="brasfoot"
    )

    cursor = cnx.cursor()

    # Execute a consulta com a cláusula WHERE
    query = ("SELECT id, nome, pontos_de_classificacao, pontos_de_forca, vitorias, derrotas, empates, gols_marcados, gols_sofridos, pontos_de_ataque, pontos_de_defesa FROM time WHERE nome = %s")
    cursor.execute(query, (nome_externo,))

    # Armazene os resultados em variáveis
    resultados = []
    for row in cursor:
        id = row[0]
        nome = row[1]
        pontos_de_classificacao = row[2]
        pontos_de_forca = row[3]
        vitorias = row[4]
        derrotas = row[5]
        empates = row[6]
        gols_marcados = row[7]
        gols_sofridos = row[8]
        pontos_de_ataque = row[9]
        pontos_de_defesa = row[10]
        resultados.append((id, nome, pontos_de_classificacao, pontos_de_forca, vitorias, derrotas, empates, gols_marcados, gols_sofridos, pontos_de_ataque, pontos_de_defesa))

    # Feche o cursor e a conexão
    cursor.close()
    cnx.close()

    # Retorne os resultados
    return resultados

'''# Use a função como desejar
resultados = consultar_time("Nome do time")
for resultado in resultados:
    id = resultado[0]
    nome = resultado[1]
    # ...'''


def consultar_ultima_rodada_simulada():
    # Conecte ao banco de dados
    cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="brasfoot"
    )

    cursor = cnx.cursor()

    # Execute a consulta
    query = ("SELECT rodada FROM ultima_rodada_simulada")
    cursor.execute(query)

    # Armazene os resultados em uma lista
    resultados = ''
    for (rodada,) in cursor:
        resultados = rodada

    # Feche o cursor e a conexão
    cursor.close()
    cnx.close()

    # Retorne os resultados
    return resultados

