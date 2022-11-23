from PySimpleGUI import PySimpleGUI as sg

# definir fonte
font_login = ('Berlin Sans FB Demi Negrito', 12)
font_login2 = ('Berlin Sans FB Demi Negrito', 10)
font_geral = ('Berlin Sans FB Demi Negrito', 15)
font_input = ('Berlin Sans FB',10)


def tela_login(user_login = '', status='',memoria=''):

    sg.theme('DarkBlue2')

    va_login = [
        [sg.Text('Usuário:',font=font_login)],
        [sg.Input(user_login, key='-user-', font=font_input, size=(20,1),
        justification='c'),sg.Image('',key='-img_v_user-')],

    ]

    va_senha = [

        [sg.Text('Senha:', font=font_login)],
        [sg.Input(key='-senha-',password_char='*', justification='c',
        font=font_input, size=(20,1)),sg.Image('',key='-img_v_senha-')]

    ]

    avi_but = [
        [sg.Button('Entrar', font=font_login, size=(7,1)),
        sg.Button('Esqueci', font=font_login, size=(7,1))]
    ]

    status_serv = [
        [sg.Image(status, key='-img_status-')]
    ]

    janela =[

        [sg.Column(layout=va_login)],

        [sg.Checkbox('Lembrar', memoria, key='-save-',font=font_input)],

        [sg.Column(layout = va_senha)],

        [sg.Text(' ', key='-info_user-',
        font=font_login, justification='c')],

        [sg.Column(layout = avi_but)],

        [sg.Column(layout=status_serv,element_justification='c')]
    ]

    return sg.Window('Login', finalize=True, size=(300,260), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c')

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

    humor = [
        [sg.Text('Qual o seu Humor do dia?', font=font_geral)],
        [sg.Text('Em uma escala de 0 até 100')],
        [sg.Slider(range=(0,100), default_value=0, orientation='h',
        size=(15,20), key='-ST_H-',enable_events=True)],
        [sg.Image('', key='-img_hu-')],
        [sg.Text(' ', key='-hu_r-', font=font_login)]
    ]

    janela =[
        [sg.Menu(bara_menu)],

        [sg.Text(f'Olá {apelido_user}!\nQual o seu Status do momento?',font=font_geral)],

        [sg.Frame('',layout=status_1,element_justification='c',key='-Add-', font=font_input)],

        [sg.HSeparator()],

        [sg.Column(humor,element_justification='c')],

        [sg.HSeparator()],

        [sg.B('Aplicar', font=font_geral), sg.B('Sair', font=font_geral, size=(6,0))],

        [sg.VPush(),sg.Text('GitHub: RTieppo', font=font_input), sg.Push(),
        sg.Push(), sg.Image('',key='-serve-'), sg.Push(), sg.Push()]

    ]
    return sg.Window('Gerenciador de Paninel', finalize=True, size=(500,520), layout = janela,
    element_justification='c', text_justification='c',margins=(0,0),icon= (r'img\icon\ico_p.ico'),
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_esqueci(status_ser):
    sg.theme('DarkBlue2')

    login_senha = [
        [sg.Text('Matrícula:',font=font_input)],
        [sg.Input(key='-mat-', font=font_input, size=(20,1),
        justification='c'),sg.Image('',key='-img_v_mat-')],

        [sg.Text('Nova Senha:', font=font_input)],
        [sg.Input(key='-senhaN1-',password_char='*', justification='c',
        font=font_input, size=(20,1)),sg.Image('',key='-img_v_ns-')],

        [sg.Text('Confirmar nova senha:', font=font_input)],
        [sg.Input(key='-senhaN2-',password_char='*', justification='c',
        font=font_input, size=(20,1)),sg.Image('',key='-img_c_ns-')]

    ]

    avi_but = [
        [sg.Button('Alterar', font=font_login,size=(7,1),pad=(10,10)),
        sg.Button('Ajuda', font=font_login,size=(7,1),pad=(10,10)),
        sg.Button('Sair', font=font_login,size=(7,1),pad=(10,10))],
    ]

    janela =[

        [sg.Column(layout=login_senha)],

        [sg.Text('', key='-info_user_es-',font=font_login)],

        [sg.HSeparator()],

        [sg.Column(layout = avi_but)],

        [sg.Image(status_ser,key='-img_status_esq-')]
    ]

    return sg.Window('Nova senha', finalize=True, size=(300,280), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c',
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

