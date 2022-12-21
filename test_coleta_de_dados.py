import DadosBancoDeDados as d
import mysql.connector

import re

import zlib
import urllib.request
import urllib.error
import os

conex = mysql.connector.connect(host=d.host,user=d.user, database=d.database,
password=d.password)


def deixa():
    if conex.is_connected():
        info = (f"select * from emoji where matricula=3090;")
        cursor = conex.cursor()
        cursor.execute(info)
        linhas = cursor.fetchall()

    dados_link = list()

    for num in linhas:
        for separa in num:
            converte = str(separa)
            if len(converte) > 8:
                dados_link.append(converte)
    
    print(dados_link)


def baixa_img_temp(link,mat):
    try:
        caminho_geral = (r'C:\Users\Public\AppPlaca')

        nome_save = ('feliz.png','cansado.png','concentrado.png','pensativo.png','serio.png')

        conta = 0

        while conta <5:
            unifica = os.path.join(caminho_geral,mat,nome_save[conta])

            img = open(f"{unifica}",'wb')
            img.write(urllib.request.urlopen(link[conta]).read())
            img.close()
            conta += 1
        
        return True
    
    except urllib.error:
        return 'Erro_ao_baixar'

texto = 'ricardo.martins@sc.senac'
padrao = re.compile(r'[a-z0-9]+\.[a-z0-9]+')
validos = padrao.finditer(texto)

for valido in validos:
    print(valido)

