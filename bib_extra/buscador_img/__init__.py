import zlib
import urllib.request
import os


def crc32(fileName):

    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)


def baixa_img():

    img = open(r'','wb')

    img.write(urllib.request.urlopen('').read())
    img.close()


def verifica_pasta_geral():

    verifica_pasta = os.listdir(r'C:\Users\Public')
    
    pasta = 'fileplaca'
    
    if pasta in verifica_pasta:
        return True
    
    else:
        return False


def verifica_verifica_pasta_user(matricula):

    verifica_pasta = os.listdir(r'C:\Users\Public\fileplaca')

    if matricula in verifica_pasta:
        return True
    
    else:
        return False


def cria_pasta_user(matricula):

    caminho = os.path.join(r'C:\Users\Public\fileplaca',matricula)

    os.makedirs(caminho)

 