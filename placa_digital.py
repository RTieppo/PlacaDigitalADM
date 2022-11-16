from PySimpleGUI import PySimpleGUI as sg
import mysql.connector
from time import sleep

from bib_extra import telas as t
from bib_extra import txt_fun as txt
from bib_extra import slq_fun as sql
import DadosBancoDeDados as d


try:
    conex = mysql.connector.connect(host=d.host, user=d.user, database=d.database,
    password=d.password)

    if conex.is_connected():
        abre_txt = txt.le_txt()
        
        if abre_txt[1] == True:
            if len(abre_txt) > 1:
                janela_login = (t.tela_login(user_login = abre_txt[0][0],
                status=(r'img\20_20\verificado.png'), memoria=abre_txt[0][1]))
                conex.close()
            
            else:
                janela_login = (t.tela_login(user_login = '',
                status= (r'img\20_20\verificado.png'), memoria=''))
                conex.close()
        else:
            janela_login = (t.tela_login(user_login = '', status= (r'img\20_20\verificado.png'),
            memoria=''))
            conex.close()

except mysql.connector.Error:
    sg.popup('        Erro de Conexão!\nVerifique o Banco De Dados',title='Error')


janela_adm = janela_esqueci= None


while True:

    window, eventos, valores = sg.read_all_windows()

    if window == janela_login and eventos == sg.WIN_CLOSED:
        break

    elif window == janela_login and eventos == 'Esqueci':
        janela_login.hide()
        janela_esqueci = t.tela_esqueci()
        

    elif window == janela_login and eventos == 'Entrar':

        verifica_user = sql.valida_user(host=d.host, user=d.user, database=d.database,
        password=d.password, user_id = valores['-user-'])

        verifica_senha = sql.valida_senha(host=d.host, user=d.user, database=d.database,
        password=d.password, senha_user = valores[str('-senha-')])


        if verifica_user and verifica_senha == True:

            window['-img_v_user-'].update(r'img\20_20\verificado.png')
            window['-img_v_senha-'].update(r'img\20_20\verificado.png')

            if valores['-save-'] == True:
                txt.cria_pasta() 
                txt.cria_txt(valores['-user-'])
            
            elif valores['-save-'] == False:
                txt.limpa_txt()

            consulta_apelido = sql.consulta_apelido(host=d.host, user=d.user,
            database=d.database, password=d.password,id_user = valores['-user-'])

            window['-info_user-'].update('Usuário valido',None,'darkgreen')
            window.refresh()
            sleep(3)

            janela_login.close()
            janela_adm = t.tela_adm(apelido_user=consulta_apelido)
        
        elif verifica_user or verifica_senha == True:

            if verifica_senha == True:
                window['-img_v_senha-'].update(r'img\20_20\verificado.png')

            if verifica_senha == False:
                window['-img_v_senha-'].update(r'img\20_20\erro.png')

            if verifica_user == True:
                window['-img_v_user-'].update(r'img\20_20\verificado.png')

            if verifica_user == False:
                window['-img_v_user-'].update(r'img\20_20\erro.png')

        else:
            window['-img_v_user-'].update('')
            window['-img_v_senha-'].update('')
            window['-info_user-'].update('Informe as Credenciais',None,'darkred')


# janela adm

    if window == janela_adm and eventos == '-ST_A-':

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.Text('Unidade:'), sg.Radio('Faculdade','-UN-', key='-FC-'),
        sg.Radio('Saúde e Beleza','-UN-', key='-SS-')]])

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.Text('Sala ou Setor:'), sg.In(key='-local-', justification='c'
        , size=(25,0))]])
        
    elif window == janela_adm and eventos == '-ST_H-':
        feliz = valores['-ST_H-']
        if feliz >= 20:
            print('Feliz')
            window['-img_hu-'].update(r'img\100_100\Feliz_100.png')
            window['-hu_r-'].update('Feliz',None,'darkgreen')
        
        print(feliz)