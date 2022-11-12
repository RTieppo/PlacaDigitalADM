from PySimpleGUI import PySimpleGUI as sg

from bib_extra import telas as t

# definir fonte
font_geral = ('Berlin Sans FB Demi Negrito', 15)
font_input = ('Berlin Sans FB',10)

janela_login = t.tela_login()
janela_adm = None

while True:
    window, eventos, valores = sg.read_all_windows(timeout=1000)

    if window == janela_login and eventos == sg.WIN_CLOSED:
        break

    elif window == janela_login and eventos == 'Entrar':
        janela_adm = t.tela_adm()
        janela_login.close()
    
    if window == janela_adm and eventos == '-ST_A-':

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.Text('Local Atendimento:')]])

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.Radio('Faculdade','-UN-', key='-FC-'),
        sg.Radio('Saúde e Beleza','-UN-', key='-SS-')]])

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.Text('Sala ou Setor:')]])

        janela_adm.extend_layout(janela_adm['-Add-'],
        [[sg.In(key='-local-', justification='c',
        font=font_input, size=(38,0))]])

        print()
