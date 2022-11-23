
def velida_senha_1(senha_1):

    if senha_1.isnumeric():
        if len(senha_1) > 1 and len(senha_1) == 4:
            return (True,senha_1)
        
        else:
            return(False, None)
    
    else:
        return(False,None)

def valida_senha_2(senha_2):

    if senha_2.isnumeric():
        if len(senha_2)>1 and len(senha_2) == 4:
            return(True,senha_2)
        
        else:
            return(False, None)
    
    else:
        return (False,None)

def valida_matricula(matricula):
    
    if matricula.isnumeric():

        if len(matricula)== 4:

            return (True,matricula)

        else:
            return(False, None)

    else:
        return (False, None)

def compara_senha():
    pass