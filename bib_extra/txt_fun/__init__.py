from os import listdir,remove


def cria_txt(id=''):
    cria_txt = open(r'C:\Users\Public\AppPlaca\login.txt', 'w', encoding='utf-8')
    cria_txt.write(f'{id},0')
    cria_txt.close()
    return True

def limpa_txt():
    valida_pasta = listdir(r'C:\Users\Public')
        
    if 'AppPlaca' in valida_pasta:
        
        valida_arquivo = listdir(r'C:\Users\Public\AppPlaca')
        
        if 'login.txt' in valida_arquivo:
            remove(r'C:\Users\Public\AppPlaca\login.txt')
    else:
        pass

def le_txt():
    valida_pasta = listdir(r'C:\Users\Public')

    if 'AppPlaca' in valida_pasta:
        valida_arquivo = listdir(r'C:\Users\Public\AppPlaca')

        if 'login.txt' in valida_arquivo:
            le = open(r'C:\Users\Public\AppPlaca\login.txt',
            'r', encoding='utf-8').read().split(',')

            return le,True

        else:
            return None,False
    
    else:
        return None,False
