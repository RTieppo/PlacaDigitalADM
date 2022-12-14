from os import makedirs, listdir,path

def cria_pasta_geral():
    while True:
        valida_pasta = listdir(r'C:\Users\Public')

        if 'AppPlaca' in valida_pasta:
            break

        else:
            makedirs(r'C:\Users\Public\AppPlaca')


def cria_pasta_user(matricula):

    caminho = path.join(r'C:\Users\Public\AppPlaca',matricula)

    makedirs(caminho)