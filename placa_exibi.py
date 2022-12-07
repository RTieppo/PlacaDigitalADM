from PySimpleGUI import PySimpleGUI as sg
from time import sleep


from bib_extra_exibi import tela_principal


inicia = tela_principal.tela_exibicao()

while True:

    window, event, values = sg.read_all_windows()

    if window == inicia and event == sg.WIN_CLOSED:
            break

