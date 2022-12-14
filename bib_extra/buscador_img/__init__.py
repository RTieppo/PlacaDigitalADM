import urllib.request
import urllib.error
from os import listdir,path


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
