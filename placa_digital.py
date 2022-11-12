from PySimpleGUI import PySimpleGUI as sg

from bib_extra import telas as t

janela_login = t.tela_login()

while True:
    window, eventos, valores = sg.read_all_windows(timeout=1000)

    if window == janela_login and eventos == sg.WIN_CLOSED:
        break