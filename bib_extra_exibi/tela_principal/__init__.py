from PySimpleGUI import PySimpleGUI as sg


def tela_exibicao():

    sg.theme('DarkBlue2')

    janela = [
        [sg.Image(open("http://t1.gstatic.com/images?q=tbn:ANd9GcRBL_Z4t3zlPVfo4WLFmVy9CE2zBLph8hmwoexfOQn1kQOHoTDAu9dLCsI4"))]
    ]


    return sg.Window('Login', finalize=True, size=(300,260), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c')