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


def verifica_os_ark(matricula):

    caminho = os.path.join(r'C:\Users\Public\fileplaca',matricula)

    conta_ark = len(os.listdir(caminho))

    if conta_ark > 0:
        return True
    
    else:
        return False



def cria_pasta_user(matricula):

    caminho = os.path.join(r'C:\Users\Public\fileplaca',matricula)

    os.makedirs(caminho)


def cria_pasta_temp():
    os.makedirs(r'C:\Users\Public\fileplaca\temp')


def deleta_ark_temp():
    pass

def deleta_temp():
    pass
