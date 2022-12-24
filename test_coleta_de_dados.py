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


def valida_user():
    texto = 'ricardo.martíns'
    padrao = r'[àèìòùáéíóúýâêîôûãñõäëïöüÿçå]'

    if '.' in texto:
        if re.search(padrao,texto):
            print(False)
        
        else:
            ajusta = texto.split('.')

            if len(ajusta) == 2:
                conta = 0
                for vare in ajusta:
                    if vare.isalpha() and vare.islower():
                        conta += 1
                
                if conta == 2:
                    print(True)

                else:
            
                    print(False)
            else:
                print(False)
    else:
        print(False)


eu = valida_user()
