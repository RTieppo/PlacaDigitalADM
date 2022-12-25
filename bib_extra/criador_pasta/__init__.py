from os import makedirs, listdir,path

def cria_pasta_geral():

    valida_pasta = listdir(r'C:\Users\Public')

    if 'AppPlaca' in valida_pasta:
        return True

    else:
        makedirs(r'C:\Users\Public\AppPlaca')


def cria_pasta_user(matricula):

    caminho = path.join(r'C:\Users\Public\AppPlaca',matricula)

    makedirs(caminho)

def cria_pasta_temp():
    
    caminho = (r'C:\Users\Public\AppPlaca\temp')
    
    makedirs(caminho)