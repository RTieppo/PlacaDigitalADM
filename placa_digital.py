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
            sg.user_settings_set_entry('-last position-', janela_login.current_location())
            window['-info_user-'].update('')
    
            test_conex = sql.BancoDeDados(host=d.host, user=d.user, database=d.database,
            password=d.password, user_id = valores['-user-'])       

            retorno_user = test_conex.valida_user()

            if retorno_user == 'Error ID':
                window['-img_status-'].update(r'img\20_20\erro.png')

            elif retorno_user[0] == True:

                test_conex = sql.BancoDeDados(host=d.host, user=d.user, database=d.database,
                password=d.password, senha_user = valores['-senha-'],
                user_id = retorno_user[1])

                retorno_senha = test_conex.valida_senha()

                if retorno_senha == 'Error Senha':
                    window['-img_status-'].update(r'img\20_20\erro.png')


                elif retorno_senha == valores['-senha-']:
                    retorno_senha = True

                    if retorno_user and retorno_senha == True:

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
                        sleep(2)

                        janela_login.close()
                        janela_adm = t.tela_adm(apelido_user=consulta_apelido)
                
                elif retorno_user[0] or retorno_senha == True:

                    if retorno_senha != True:
                        window['-img_v_senha-'].update(r'img\20_20\erro.png')

                    if retorno_user[0] == True:
                        window['-img_v_user-'].update(r'img\20_20\verificado.png')
                
                else:
                    window['-img_v_senha-'].update(r'img\20_20\erro.png')

            elif retorno_user[0] == False:
                window['-img_v_user-'].update(r'img\20_20\erro.png')

        elif window == janela_login and eventos == 'Esqueci':
            sg.user_settings_set_entry('-last position-', janela_login.current_location())
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

        elif window == janela_esqueci and eventos == 'Sair':
            sg.user_settings_set_entry('-last position-', janela_esqueci.current_location())
            janela_esqueci.close()
            janela_login.un_hide()

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
roda_app(inicia)


