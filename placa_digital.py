from PySimpleGUI import PySimpleGUI as sg

from bib_extra import telas as t
from bib_extra import slq_fun as sql
from bib_extra import txt_fun as txt

def valida_info():
    #validação do servidor
    teste_conec = sql.valida_ser()

    if teste_conec[1] == True:
        abre_txt = txt.le_txt()
        print(len(abre_txt))

        if len(abre_txt) > 1:
            janela_login = (t.tela_login(user_login = abre_txt[0], status= teste_conec[0],
            memoria=abre_txt[1]))
        
        else:
            janela_login = (t.tela_login(user_login = '', status= teste_conec[0],
            memoria=''))

    else:
        sg.Popup('Erro na conecção do servidor\n contate o administrador')
    
    return janela_login

def start_login(janela_login):

    while True:

        window, eventos, valores = sg.read_all_windows(timeout=1000)

        if window == janela_login and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_login and eventos == 'Esqueci':
            pass

        elif window == janela_login and eventos == '-save-':

            pass

        elif window == janela_login and eventos == 'Entrar':
            
            verifica_user = sql.valida_user(valores['-user-'])

            verifica_senha = sql.valida_senha(valores[str('-senha-')])

            if verifica_user and verifica_senha == True:
                if valores['-save-'] == True:
                    txt.cria_txt(valores['-user-'])
                    janela_login.close()
                    janela_adm = t.tela_adm(apelido_user='')
                
                return janela_adm      
            
            else:
                print('erro')


def start_adm(janela_adm):

    while True:
        window, eventos, valores = sg.read_all_windows(timeout=1000)

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

validador = valida_info()

star_1 = start_login(validador)

star_2 = start_adm(star_1)