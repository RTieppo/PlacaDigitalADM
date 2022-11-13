import pymysql.cursors

con = pymysql.connect(host='localhost', user='root', database='painel_digital', password='root', cursorclass=pymysql.cursors.DictCursor)

with con.cursor() as c:
    info = 'Select * from login;'
    c.execute(info)
    resposta = c.fetchone()
    print(resposta['nome'])
