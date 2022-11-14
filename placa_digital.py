from PySimpleGUI import PySimpleGUI as sg

from bib_extra import telas as t
from bib_extra import slq_fun as sql

teste_conec = sql.valida_ser()

janela_login = t.tela_login(user_login = '',user_senha='', status= teste_conec[0])
janela_adm = None

while True:
    window, eventos, valores = sg.read_all_windows(timeout=1000)

    if window == janela_login and eventos == sg.WIN_CLOSED:
        break

    elif window == janela_login and eventos == 'Esqueci':
        pass

    elif window == janela_login and eventos == '-save-'

    elif window == janela_login and eventos == 'Entrar':

        verifica_user = sql.valida_user(valores['-user-'])

        verifica_senha = sql.valida_senha(valores[str('-senha-')])
    
        
        


    
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