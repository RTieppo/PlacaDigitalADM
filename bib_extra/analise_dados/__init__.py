
class ValidaDados:

    def __init__(self,matricula='',nome='',apelido='',id='',senha='',nivel=''):

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
            if len(self.matricula)== 4:
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
    
    def valida_novo_id(self):

        if self.id.isalpha():
            if len(self.id) >1 and len (self.id) <=10:
                return True
            
            else:
                return False

        else:
            return False

    def valida_senha(self):
        
        senha1 = senha2 = None

        if len(self.senha) == 2:

            if self.senha[0].isnumeric():
                senha1 = True
            else:
                senha1 = False

            if self.senha[1].isnumeric():
                senha2 = True
            
            else:
                senha2 = False

            return senha1,senha2

        elif self.senha.isnumeric():
            if len(self.senha) == 4:
                return True
            
            else:
                return False
        else:
            return False
    