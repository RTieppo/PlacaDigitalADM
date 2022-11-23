from PySimpleGUI import PySimpleGUI as sg
from time import sleep
from mysql.connector import Error
import mysql.connector

from bib_extra import telas as t
from bib_extra import txt_fun as txt
from bib_extra import slq_fun as sql
from bib_extra import analise_dados as dados
import DadosBancoDeDados as d


def start_serve():
    global test_conex

    test_conex = sql.BancoDeDados(host=d.host, user=d.user, database=d.database,
        password=d.password)       

    retorno = test_conex.conecta()

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


def roda_app(star):
    global test_conex

    janela_login = star

    janela_adm = janela_esqueci =  None

    erro = (r'img\20_20\erro.png')
    verificado = (r'img\20_20\verificado.png')
    
    while True:

        window, eventos, valores = sg.read_all_windows()

        if window == janela_login and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_login and eventos == 'Entrar':
            sg.user_settings_set_entry('-last position-', janela_login.current_location())
            window['-info_user-'].update('')

            retorno_test = test_conex.consulta_conex()

            if retorno_test == True:

                retorno_user = test_conex.consulta_user(user_id = valores['-user-'])

                if retorno_user == 'Error ID':
                    window['-img_status-'].update(r'img\20_20\erro.png')

                elif retorno_user[0] == True:

                    retorno_senha = test_conex.consulta_senha(user_id = retorno_user[1])

                    if retorno_senha == 'Error Senha':
                        window['-img_status-'].update(erro)

                    elif retorno_senha == valores['-senha-']:
                        retorno_senha = True

                        if retorno_user and retorno_senha == True:

                            window['-img_v_user-'].update(verificado)
                            window['-img_v_senha-'].update(verificado)

                            if valores['-save-'] == True:
                                txt.cria_pasta() 
                                txt.cria_txt(valores['-user-'])
                            
                            elif valores['-save-'] == False:
                                txt.limpa_txt()

                            consulta_apelido = test_conex.consulta_apelido(id_user = valores['-user-'])

                            window['-info_user-'].update('Usuário valido',None,'darkgreen')
                            window.refresh()
                            sleep(1)
                            window['-info_user-'].update('Acessando...',None,'darkgreen')
                            window.refresh()
                            sleep(1)

                            janela_login.close()
                            janela_adm = t.tela_adm(apelido_user=consulta_apelido)
                            #colocar tratamento para erro de apelido
                    
                    elif retorno_user[0] or retorno_senha == True:

                        if retorno_senha != True:
                            window['-img_v_senha-'].update(erro)

                        if retorno_user[0] == True:
                            window['-img_v_user-'].update(verificado)
                    
                    else:
                        window['-img_v_senha-'].update(erro)

                elif retorno_user[0] == False:
                    window['-img_v_user-'].update(erro)
            
            else:
                window['-img_status-'].update(erro)

        elif window == janela_login and eventos == 'Esqueci':

            retorno = test_conex.consulta_conex()

            if retorno == True:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(verificado)
            
            elif retorno == False:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(erro)

    #Janela esqueci senha

        if window == janela_esqueci and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_esqueci and eventos == 'Sair':
            sg.user_settings_set_entry('-last position-', janela_esqueci.current_location())
            janela_esqueci.close()
            janela_login.un_hide()

        elif window == janela_esqueci and eventos == 'Alterar':

            window['-info_user_es-'].update('')
            window['-img_v_mat-'].update('')
            window['-img_v_ns-'].update('')
            window['-img_c_ns-'].update('')

            matricula = dados.valida_matricula(valores['-mat-'])

            if matricula[0] == True:

                consulta = test_conex.consulta_matricula(matricula=matricula[1])
                print(consulta)

                if consulta[0] == True:
                    window['-img_v_mat-'].update(verificado)
                
                elif consulta[1] == 'Error matricula':
                    window['-img_status_esq-'].update(erro)
                
                else:
                    window['-img_v_mat-'].update(erro)

            else:
                window['-img_v_mat-'].update(erro)

            senha_1 = dados.velida_senha_1(valores['-senhaN1-'])
            if senha_1[0] == True:
                window['-img_v_ns-'].update(verificado)

            else:
                window['-img_v_ns-'].update(erro)

            senha_2 = dados.valida_senha_2(valores['-senhaN2-'])

            if senha_2[0] == True:
                window['-img_c_ns-'].update(verificado)
            
            else:
                window['-img_c_ns-'].update(erro)

            window.refresh()
            sleep(2)

            if senha_1[0] == True and senha_2[0] == True and consulta[0] == True:

                if senha_1[1] == senha_2[1]:

                    window['-info_user_es-'].update('Dados validos!', None,'darkgreen')
                    window.refresh()
                    sleep(2)
                    window['-info_user_es-'].update('Atualizando!', None,'darkgreen')
                    altera_senha = test_conex.altera_senha(n_senha=senha_1[1], matricula=valores['-mat-'])
                    window.refresh()
                    sleep(1)

                    if altera_senha == True:
                        test_conex.reconecta()
                        window['-info_user_es-'].update('Senha alterada!', None,'darkgreen')
                    
                    elif altera_senha == 'Erro alteração senha':
                        window['-img_status_esq-'].update(erro)
                    
                    else:
                        window['-info_user_es-'].update('Erro na alteração!', None,'darkred')

                else:
                    window['-img_v_ns-'].update(erro)
                    window['-img_c_ns-'].update(erro)
           
    # janela adm

        if window == janela_adm and eventos == sg.WIN_CLOSED or janela_adm and eventos == 'Sair':
            break

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

