import DadosBancoDeDados as d
import mysql.connector

import zlib
import urllib.request
import os

conex = mysql.connector.connect(host=d.host,user=d.user, database=d.database,
password=d.password)

if conex.is_connected():
    info = (f"select * from emoji where matricula=3090;")
    cursor = conex.cursor()
    cursor.execute(info)
    linhas = cursor.fetchall()

dados_crc32 = list()

for num in linhas:
    for separa in num[1:]:
        converte = str(separa)
        if converte.isalnum():
            dados_crc32.append(converte)
 
print(dados_crc32)






if conex.is_connected():
    info = (f"select * from emoji where matricula=3090;")
    cursor = conex.cursor()
    cursor.execute(info)
    linhas = cursor.fetchall()

dados_link = list()

for num in linhas:
    for separa in num[2:]:
        converte = str(separa)
        if len(converte) > 8:
            dados_link.append(converte)
 
print(dados_link)


def baixa_img_temp(link):
    ark =(r'C:\Users\Public\fileplaca\temp\feliz.png',
    r'C:\Users\Public\fileplaca\temp\cansado.png',r'C:\Users\Public\fileplaca\temp\concentrado.png',
    r'C:\Users\Public\fileplaca\temp\pensativo.png',r'C:\Users\Public\fileplaca\temp\serio.png')
    
    conta = 0

    while conta <5:
        img = open(f"{ark[conta]}",'wb')
        img.write(urllib.request.urlopen(link[conta]).read())
        img.close()
        conta += 1
    
    print('ok')

baixa_img_temp(dados_link)