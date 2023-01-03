
from os import listdir,path
import cv2

def verifica_pasta_user(matricula):

    verifica_pasta = listdir(r'C:\Users\Public\AppPlaca')

    if matricula in verifica_pasta:
        return True
    
    else:
        return False

def verifica_ark_img(matricula):
    
    caminho_geral = (r'C:\Users\Public\AppPlaca')
    unifica_caminho = path.join(caminho_geral,matricula)

    lista_ark = listdir(unifica_caminho)

    if len (lista_ark) == 5:
        return True
    
    else:
        return False


def verifica_pasta_temp():
    
    valida_pasta = listdir(r'C:\Users\Public\AppPlaca')

    if 'temp' in valida_pasta:
        return True
    
    else:
        return False

def ajusta_img(matricula,ark):

    caminho_geral = (r'C:\Users\Public\AppPlaca')
    unifica_caminho = path.join(caminho_geral,matricula,ark)
    
    imagem = cv2.imread(unifica_caminho)

    imagem = cv2.resize(imagem,dsize=(120,120))

    temp = (r'C:\Users\Public\AppPlaca\temp\img.png')

    cv2.imwrite(temp,imagem)

    return temp
    
