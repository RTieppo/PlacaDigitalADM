import mysql.connector
from PySimpleGUI import popup
from mysql.connector import Error

class BancoDeDadosConsultor:
    def __init__(self,host,user, database, password,user_id = None, senha_user = None,
    matricula = None):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.user_id = user_id
        self.senha_user = senha_user
        self.matricula = matricula

    def consulta_conex(self):

        try:
            conex = mysql.connector.connect(host = self.host, user = self.user,
            database = self.database, password = self.password)

            if conex.is_connected():
                conex.close()
                return (True,r'img\20_20\verificado.png')
            
            else:
                return (False,r'img\20_20\erro.png')
                
        except Error as err:
            return (False,err)
        
    def consulta_user(self):

        try:
            conex = mysql.connector.connect(host = self.host, user = self.user,
            database = self.database, password = self.password)

            info = ('select id_user from login;')
            cursor = conex.cursor()
            cursor.execute(info)
            linhas = cursor.fetchall()

            for linha in linhas:
                if self.user_id in linha:
                    conex.close()
                    return (True, self.user_id)
            else:
                conex.close()
                return (False,None)

        except Error:
            return ('Error ID',None)

    def consulta_senha(self):

        try:
            conex = mysql.connector.connect(host = self.host, user = self.user,
            database = self.database, password = self.password)

            info = (f"select senha from login where id_user = '{self.user_id}';")
            cursor = conex.cursor()
            cursor.execute(info)
            linhas = cursor.fetchone()

            conex.close()
            return (str(linhas[0]))


        except Error:
            return 'Error Senha'

    def consulta_matricula(self):
        
        try:
            conex = mysql.connector.connect(host = self.host, user = self.user,
            database = self.database, password = self.password)

            info = ('select matricula from login order by nome;')
            cursor = conex.cursor()
            cursor.execute(info)
            linhas = cursor.fetchall()
            
            for linha in linhas:
                for le in linha:
                    converte = str(le)
                    print(converte)

                    if converte == self.matricula:
                        return (True, converte)
                
            else:
                return (False,None)
                
        except Error:
            return 'Error matricula'


def consulta_apelido(host,user, database, password,id_user):
    try:
        conex = mysql.connector.connect(host=host, user=user, database=database,
        password=password)

        info = (f"select apelido from login where id_user='{id_user}';")
        cursor = conex.cursor()
        cursor.execute(info)
        linhas = cursor.fetchall()

        conex.close()
        return linhas[0][0]

    except Error:
        return 'erro apelido'

class BancoDeDadosAltera:

    def __init__(self,host,user, database, password,user_id = None, senha_user = None,
    matricula = None):

        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.user_id = user_id
        self.senha_user = senha_user
        self.matricula = matricula

    
    def altera_senha(self,n_senha):
        try:
            conex = mysql.connector.connect(host = self.host, user = self.user,
            database = self.database, password = self.password)

            alterador = (f"update login set senha='{n_senha}' where matricula='{self.matricula}';")
            cursor = conex.cursor()
            cursor.execute(alterador)
            conex.commit()
            conex.close()
            return True

        except Error as erro:
            return 'Erro alteração senha'
