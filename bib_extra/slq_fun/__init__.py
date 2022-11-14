import pymysql.cursors

con = pymysql.connect(host='localhost', user='root',
        database='painel_digital', password='root',
        cursorclass= pymysql.cursors.DictCursor)


def valida_ser():
    try:
        if con.cursor():
            return (r'img\icon\verificado.ico','yes')
    
    except Exception:
        return (r'img\icon\erro.ico','error')
    
    con.close()

def valida_user(user=''):

    with con.cursor() as c:
        info = 'select id_user from login;'
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

