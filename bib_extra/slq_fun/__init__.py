import mysql.connector
from PySimpleGUI import popup
from mysql.connector import Error

class BancoDeDados:
    def __init__(self,host,user, database, password, user_id = None, senha_user = None,
    matricula = None):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.user_id = user_id
        self.senha_user = senha_user
        self.matricula = matricula

    
    def conecta(self):
        global conex
        try:
            conex = mysql.connector.connect(host = self.host ,user = self.user,
            database = self.database, password = self.password)

            if conex.is_connected():
                return (True,r'img\20_20\verificado.png')

            else:
                return (False,r'img\20_20\erro.png')

        except Error as erro:
            return popup(erro,title='Erro durante conexão')

    def reconecta(self):
        try:

            if conex.is_connected():
                return (True, 'tava')
            
            else:
                conex.connect()

                if conex.is_connected():
                    return (True,'volto')
        
        except Error:
            return False

    def consulta_conex(self):

        try:
            if conex.is_connected():
                return True
            
            else:
                return False
                
        except Error:
            return False
        
    def consulta_user(self,user_id):

        try:
            if conex.is_connected():
                info = ('select id_user from login;')
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()

                for linha in linhas:
                    if user_id in linha:
                        return (True, user_id)
                else:
                    return (False,None)
            
            else:
                return(False,None)

        except Error:
            return ('Error ID',None)

    def consulta_senha(self,user_id):

        try:
            if conex.is_connected():

                info = (f"select senha from login where id_user = '{user_id}';")
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchone()
                
                return (str(linhas[0]))

        except Error:
            return 'Error Senha'

    def consulta_matricula(self, matricula):
        
        try:
            if conex.is_connected():

                info = ('select matricula from login order by nome;')
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()
                
                for linha in linhas:
                    for le in linha:
                        converte = str(le)

                        if converte == matricula:
                            return (True, converte)
                    
                else:
                    return (False,None)

        except Error as erro:
            return (False,'Error matricula')

    def consulta_apelido(self,id_user):
        try:
            if conex.is_connected():

                info = (f"select apelido from login where id_user='{id_user}';")
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()
                return linhas[0][0]

        except Error:
            return 'erro apelido'
            
    def altera_senha(self,n_senha,matricula):
        try:
           
           if conex.is_connected():

                alterador = (f"update login set senha='{n_senha}' where matricula='{matricula}';")
                cursor = conex.cursor()
                cursor.execute(alterador)
                conex.commit()
                conex.close()
                return True

        except Error:
            return 'Erro alteração senha'
