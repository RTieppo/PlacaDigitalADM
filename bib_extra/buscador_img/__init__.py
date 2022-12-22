import urllib.request
import urllib.error
from os import listdir,path

import cv2


def baixa_img(link,mat):

    try:
        caminho_geral = (r'C:\Users\Public\AppPlaca')

        nome_save = ('feliz.png','cansado.png','concentrado.png','pensativo.png','serio.png')

        conta = 0

        while conta <5:
            unifica = path.join(caminho_geral,mat,nome_save[conta])
            
            img = open(f"{unifica}",'wb')
            img.write(urllib.request.urlopen(link[conta]).read())
            img.close()
            conta += 1
        
        return True
    
    except urllib.error:
        return 'Erro_img'



def verifica_pasta_user(matricula):

    verifica_pasta = listdir(r'C:\Users\Public\AppPlaca')

    if matricula in verifica_pasta:
        return True
    
    else:
        return False


def ajusta_img():
    
    imagem = cv2.imread(r'img\original\3090\cansado.png')

    imagem = cv2.resize(imagem[150,150])

    temp = ('temp/img.png')

    cv2.imwrite(temp,imagem)
    
