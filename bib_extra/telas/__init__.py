from PySimpleGUI import PySimpleGUI as sg

# definir fonte

def tela_login(user_login = '',user_senha=''):

    sg.theme('Black')

    janela =[
        [sg.Text('Usuário:'), sg.Input(user_login, key='-user-')],
        [sg.Text('Senha:'), sg.Input(user_senha, key='-senha-',password_char='*')],
        [sg.Text(' ', key='-info_user-')],
        [sg.Checkbox('Lembrar')],
        [sg.Button('Entrar'), sg.Button('Sair')]
    ]
    return sg.Window('Login', finalize=True, size=(300,300), layout = janela, element_justification='c')