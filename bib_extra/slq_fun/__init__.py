import pymysql.cursors
import pymysql.err


def valida_ser():
    global con
    try:
        con = pymysql.connect(host='localhost', user='root',
        database='painel_digital', password='root',
        cursorclass= pymysql.cursors.DictCursor)

        if con.cursor():
            return (r'img\icon\verificado.ico',True)
    
    except pymysql.err.OperationalError:
        return (r'img\icon\erro.ico',False)
    
    except Exception:
        return (r'img\icon\erro.ico',False)
    
    con.close()

def valida_user(user=''):

    with con.cursor() as c:
        info = ('select id_user from login;')
        c.execute(info)
        resposta = c.fetchall()

    for linha in resposta:
        if linha['id_user'] == user:
            return True
    else:
        return False

def valida_senha(senha=''):

    with con.cursor() as c:
        info = 'Select senha from login;'
        c.execute(info)
        resposta = c.fetchall()

    for linha in resposta:
        if linha['senha'] == senha:
            return True

    else:
        return False

