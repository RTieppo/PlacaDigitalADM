import os

def cria_pasta():
    while True:
        valida_pasta = os.listdir(r'C:\Users\Public')

        if 'fileplaca' in valida_pasta:
            break

        else:
            os.makedirs(r'C:\Users\Public\fileplaca')

def cria_txt(id=''):
    cria_txt = open(r'C:\Users\Public\fileplaca\login.txt', 'w', encoding='utf-8')
    cria_txt.write(f'{id},0')
    cria_txt.close()
    return True

def le_txt():

    le = open(r'C:\Users\Public\fileplaca\login.txt', 'r', encoding='utf-8').read().split(',')

    return le