from PySimpleGUI import PySimpleGUI as sg
from time import sleep
from mysql.connector import Error
import mysql.connector

from bib_extra import telas as t
from bib_extra import txt_fun as txt
from bib_extra import slq_fun as sql
import DadosBancoDeDados as d

def start_serve():
    test_conex = sql.BancoDeDados(host=d.host, user=d.user, database=d.database,
        password=d.password)       

    retorno = test_conex.testa_conec_serv()

    if retorno[0] == True:
        abre_txt = txt.le_txt()
        
        if abre_txt[1] == True:
            if len(abre_txt) > 1:
                return (t.tela_login(user_login = abre_txt[0][0],
                status=retorno[1], memoria=abre_txt[0][1]))
            
            else:
                return (t.tela_login(user_login = '',
                status= retorno[1], memoria=''))

        else:
            return (t.tela_login(user_login = '', status= retorno[1],
            memoria=''))

    else:
        sg.popup_error('Erro de Conexão! Verifique o Banco De Dados',retorno[1],title='Error')

def roda_app(star):

    janela_login = star

    janela_adm = janela_esqueci =  None
    
    while True:

        window, eventos, valores = sg.read_all_windows()

        if window == janela_login and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_login and eventos == 'Entrar':
            window['-info_user-'].update('')

            verifica_user = sql.valida_user(host=d.host, user=d.user, database=d.database,
            password=d.password, user_id = valores['-user-'])

            if verifica_user == 'Error ID':
                window['-img_status-'].update(r'img\20_20\erro.png')

            elif verifica_user == True:

                verifica_senha = sql.valida_senha(host=d.host, user=d.user, database=d.database,
                password=d.password, senha_user = valores[str('-senha-')])

                if verifica_senha == 'Error Senha':
                    window['-img_status-'].update(r'img\20_20\erro.png')

                elif verifica_user and verifica_senha == True:

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
                window['-info_user-'].update('Credenciais inválidas!',None,'darkred')

        elif window == janela_login and eventos == 'Esqueci':
            test_conex = sql.BancoDeDados(host=d.host, user=d.user, database=d.database,
            password=d.password)

            retorno = test_conex.testa_conec_serv()

            if retorno[0] == True:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(retorno[1])
            
            elif retorno[0] == False:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(retorno[1])

            else:
                sg.popup('Erro com o Banco de Dados',retorno[1],title='Error')


    #Janela esqueci senha

        if window == janela_esqueci and eventos == sg.WIN_CLOSED:
            break


    # janela adm

        elif window == janela_adm and eventos == '-ST_A-':

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


inicia = start_serve()

if inicia != None:
    roda_app(inicia)


