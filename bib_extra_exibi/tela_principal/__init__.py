from PySimpleGUI import PySimpleGUI as sg

def tela_exibicao():

    sg.theme('DarkBlue2')

    janela = [
        [sg.Image(img,size=(300, 300), key='-IMAGE-')]
    ]


    return sg.Window('Login', finalize=True, size=(300,260), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c')