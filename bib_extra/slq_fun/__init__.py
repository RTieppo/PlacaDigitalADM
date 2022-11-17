import mysql.connector
from mysql.connector import Error

def testa_conec_serv(host,user, database, password, user_id=''):
    try:
        conex = mysql.connector.connect(host=host, user=user, database=database,
        password=password)

        if conex.is_connected():
            conex.close()
            return (r'img\20_20\verificado.png')
        
        else:
            conex.close()
            return (r'img\20_20\erro.png')
            
    except Error:
        conex.close()
        return 'Erro Id'



def valida_user(host,user, database, password, user_id=''):

    try:
        conex = mysql.connector.connect(host=host, user=user, database=database,
        password=password)

        info = ('select id_user from login;')
        cursor = conex.cursor()
        cursor.execute(info)
        linhas = cursor.fetchall()

        for linha in linhas:
            if user_id in linha:
                conex.close()
                return True
        else:
            conex.close()
            return False

    except Error:
        return 'Error ID'

def valida_senha(host,user, database, password,senha_user=''):

    try:
        conex = mysql.connector.connect(host=host, user=user, database=database,
        password=password)

        info = ('select senha from login;')
        cursor = conex.cursor()
        cursor.execute(info)
        linhas = cursor.fetchall()

        for linha in linhas:
            if senha_user in linha:
                conex.close()
                return True
        else:
            conex.close()
            return False

    except Error:
        return 'Error Senha'

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
        return 'error'
