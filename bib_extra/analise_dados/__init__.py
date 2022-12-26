import re

class ValidaDados:

    def __init__(self,matricula='',id='',senha=''):

        self.matricula = matricula
        self.id = id
        self.senha = senha

    
    def valida_matricula(self):

        if self.matricula.isnumeric():
            if len(self.matricula)== 4:
                return True
            
            else:
                return False
        
        else:
            return False
  
    def valida_novo_id(self):

        padrao = r'[àèìòùáéíóúýâêîôûãñõäëïöüÿçå]'

        if '.' in self.id:

            if re.search(padrao,self.id):
                return False
            
            else:
                ajusta = self.id.split('.')

                if len(ajusta) == 2:
                    conta = 0
                    for vare in ajusta:
                        if vare.isalpha() and vare.islower():
                            conta += 1
                    
                    if conta == 2:
                        return True

                    else:
                
                        return False
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


def valida_link(link):
    
    padrao = (r'(https://)?[a-z0-9/_.]+.png')
    
    if re.search(padrao,link):
        return True
    
    else:
        return False