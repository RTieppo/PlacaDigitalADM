import mysql.connector
from PySimpleGUI import popup
from mysql.connector import Error


conex = mysql.connector.connect(host = '10.10.99.24', user = 'root', database = 'painel_digital', password = 'root')

 
if conex.is_connected():
    print('sim')
    conex.close()
if conex.is_closed():
    print('fechado')