from PySimpleGUI import PySimpleGUI as sg

# definir fonte
font_geral = ('Berlin Sans FB Demi Negrito', 15)
font_input = ('Berlin Sans FB',10)

def tela_login(user_login = '',user_senha=''):

    sg.theme('DarkBlue2')

    janela =[
        [sg.Text('Usuário:',font=font_geral)],

        [sg.Input(user_login, key='-user-', justification='c', font=font_input)],

        [sg.Text('Senha:', font=font_geral)],

        [sg.Input(user_senha, key='-senha-',password_char='*', justification='c',
        font=font_input)],

        [sg.Checkbox('Lembrar',font=font_geral)],

        [sg.Text(' ', key='-info_user-', font=font_geral)],

        [sg.Button('Entrar', font=font_geral), sg.Button('Sair', font=font_geral)]
    ]
    return sg.Window('Login', finalize=True, size=(300,250), layout = janela,
    element_justification='c', text_justification='c',margins=(0,0))


def tela_adm(apelido_user=''):

    sg.theme('DarkBlue2')

    bara_menu =[
        ['Menu',['Alterar',['ID','Senha','Apelido','Permição']]],
        ['Cadastro',['Novo user','Aviso','Informativo']],
        ['Help',['About']]
    ]

    status_1 = [
        [sg.Radio('Atendando','ST1', key='-ST_A-',enable_events=True),
        sg.Radio('Disponível', 'ST1', key='-ST_D-'),
        sg.Radio('Reunião','ST1',key='ST_R')],

        [sg.Radio('WC','ST1',key='-ST_W-'),
        sg.Radio('Almoço','ST1',key='-ST_AL-'),
        sg.Radio('Café','ST1',key='-ST_CF-')]
    ]

    janela =[
        [sg.Menu(bara_menu)],

        [sg.Text(f'Olá {apelido_user}!\nQual o seu Status do momento?',font=font_geral)],

        [sg.Frame('',layout=status_1,element_justification='c',key='-Add-', font=font_input)],

        [sg.Text('=='*50)],

        [sg.Text('Qual o seu Humor do dia?', font=font_geral)],
        [sg.Text('Em uma escala de 0 até 100')],
        [sg.Slider(range=(0,100), default_value=0, orientation='h',
        size=(15,20), key='-ST_H-')],

        [sg.Text('=='*50)],

        [sg.B('Aplicar', font=font_geral), sg.B('Sair', font=font_geral)]


    ]
    return sg.Window('Gerenciador de Paninel', finalize=True, size=(500,500), layout = janela,
    element_justification='c', text_justification='c',margins=(0,0))