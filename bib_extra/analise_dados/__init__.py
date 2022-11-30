
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


class ValidaDadosNovoUser:

    def __init__(self,matricula,nome,apelido,id,senha,nivel):

        self.matricula = matricula
        self.nome = nome
        self.apelido = apelido
        self.id = id
        self.senha = senha
        self.nivel = nivel
    

    def valida_nome(self):

        if self.nome.isalpha():

            if len(self.nome) >1 and len(self.nome) <=30:
                return True
            
            else:
                return False
        else:
            return False
    
    def valida_matricula(self):

        if self.matricula.isnumeric():
            if len(self.matricula) >1 and len(self.matricula)== 4:
                return True
            
            else:
                return False
        
        else:
            return False

    def valida_apelido(self):
        
        if len(self.apelido) >1 and len (self.apelido) <=10:
            return True
        
        else:
            return False
    
    def valida_senha(self):

        if self.senha.isnumeric():
            if len(self.senha) >1 and len(self.senha) == 4:
                return True
            
            else:
                return False
        else:
            return False
    
    