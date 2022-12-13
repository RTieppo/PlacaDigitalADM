import DadosBancoDeDados as d
import mysql.connector

conex = mysql.connector.connect(host=d.host,user=d.user, database=d.database,
password=d.password)

if conex.is_connected():
    info = (f"select * from emoji where matricula=3090;")
    cursor = conex.cursor()
    cursor.execute(info)
    linhas = cursor.fetchall()

dados = list()

for num in linhas:
    for separa in num[1:]:
        converte = str(separa)
        if converte.isalnum():
            dados.append(converte)
print(dados)
