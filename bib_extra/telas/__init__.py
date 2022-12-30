from PySimpleGUI import PySimpleGUI as sg

# definir fonte
font_login = ('Berlin Sans FB Demi Negrito', 12)
font_login2 = ('Berlin Sans FB Demi Negrito', 10)
font_geral = ('Berlin Sans FB Demi Negrito', 15)
font_input = ('Berlin Sans FB',12)


def tela_login(user_login = '', status='',memoria=''):

    sg.theme('DarkBlue2')

    va_login = [
        [sg.Text('Usuário:',font=font_login)],
        [sg.Input(user_login, key='-user-', font=font_input, size=(20,1),
        justification='c'),sg.Image('',key='-img_v_user-')],

    ]

    va_senha = [

        [sg.Text('Senha:', font=font_login)],
        [sg.Input(key='-senha-',enable_events=True,password_char='*', justification='c',
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

    return sg.Window('Login', finalize=True, size=(300,280), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c')

def tela_adm(apelido_user=''):

    sg.theme('DarkBlue2')

    bara_menu =[
        ['Menu',['Alterar',['Senha'],
        'Cadastro',['Aviso','Emoji','Informativo','Novo user']]],
        ['Help',['About','Cadastro emoji']]
    ]

    status_1 = [
        [sg.Radio('Atendando','ST1', key='-ST_A-',enable_events=True),
        sg.Radio('Disponível', 'ST1', key='-ST_D-',enable_events=True),
        sg.Radio('Reunião','ST1',key='ST_R',enable_events=True)],

        [sg.Radio('Volto logo','ST1',key='-ST_volto-',enable_events=True),
        sg.Radio('Intervalo','ST1',key='-ST_int-',enable_events=True)],

        [sg.Text('Unidade:'),sg.Radio('Faculdade','-UN-', key='-FC-',enable_events=True),
        sg.Radio('Saúde e Beleza','-UN-', key='-SS-',enable_events=True)],

        [sg.Text('Sala ou Setor:'), sg.In(key='-local-',
        justification='c', size=(25,0),enable_events=True)]

    ]

    humor = [
        [sg.Text('Qual o seu Humor do dia?', font=font_geral)],
        [sg.Text('Em uma escala de 0 até 5')],
        [sg.Slider(range=(0,5), default_value=0, orientation='h',
        size=(15,20), key='-ST_H-',enable_events=True)],
        [sg.Image('', key='-img_hu-')],
        [sg.Text(' ', key='-hu_r-', font=font_login)]
    ]

    janela =[
        [sg.Menu(bara_menu)],

        [sg.Text(f'Olá {apelido_user}!\nQual o seu Status do momento?',font=font_geral)],

        [sg.Frame('',layout=status_1,element_justification='c',font=font_input)],

        [sg.HSeparator()],

        [sg.Column(humor,element_justification='c')],

        [sg.HSeparator()],

        [sg.Text('',key='-info_adm-', font=font_input)],

        [sg.B('Aplicar', font=font_geral),sg.B('Logoff', font=font_geral, size=(6,0)) ,sg.B('Sair', font=font_geral, size=(6,0))],

        [sg.Image('',key='-serve-')]

    ]
    return sg.Window('Gerenciador de Paninel', finalize=True, size=(500,540), layout = janela,
    element_justification='c', text_justification='c',margins=(0,0),icon= (r'img\icon\ico_p.ico'),
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_esqueci(status_ser):
    sg.theme('DarkBlue2')

    login_senha = [
        [sg.Text('Matrícula:',font=font_input)],
        [sg.Input(key='-mat-', font=font_input, size=(20,1),
        justification='c',enable_events=True),sg.Image('',key='-img_v_mat-')],

        [sg.Text('Nova Senha:', font=font_input)],
        [sg.Input(key='-senhaN1-',password_char='*', justification='c',
        font=font_input, size=(20,1), enable_events=True),sg.Image('',key='-img_v_ns-')],

        [sg.Text('Confirmar nova senha:', font=font_input)],
        [sg.Input(key='-senhaN2-',password_char='*', justification='c',
        font=font_input, size=(20,1),enable_events=True),sg.Image('',key='-img_c_ns-')]

    ]

    avi_but = [
        [sg.Button('Alterar', font=font_login,size=(7,1),pad=(10,10)),
        sg.Button('Ajuda', font=font_login,size=(7,1),pad=(10,10)),
        sg.Button('Voltar', font=font_login,size=(7,1),pad=(10,10))],
    ]

    janela =[

        [sg.Column(layout=login_senha)],

        [sg.Text('', key='-info_user_es-',font=font_login)],

        [sg.HSeparator()],

        [sg.Column(layout = avi_but)],

        [sg.Image(status_ser,key='-img_status_esq-')]
    ]

    return sg.Window('Nova senha', finalize=True, size=(300,300), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c',
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_novo_user(status_ser):

    sg.theme('DarkBlue2')

    entradas = [
        [sg.Text('Matricula:', font=font_input)],
        [sg.Input(key='-n_mat-', justification='c',font=font_input,size=(20,1),
        enable_events=True),
        sg.Image('',key='-img_n_mat-')],

        
        [sg.Text('ID:', font=font_input)],
        [sg.Input(key='-n_id-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-img_n_id-')]

        ]

    botoes = [
        [sg.B('Aplicar', font=font_login,size=(7,1),pad=(10,10)),
        sg.B('Ajuda',font=font_login,size=(7,1),pad=(10,10)),
        sg.B('Voltar', font=font_login, size=(7,1),pad=(10,10))]
    ]

    janela =[

        [sg.Column(layout=entradas)],

        [sg.Text('',key='-info_n_ca-', font=font_login)],

        [sg.Column(layout=botoes)],


        [sg.Image(status_ser,key='-img_status_esq-')]

    ]

    return sg.Window('Novo cadastro', finalize=True, size=(300,250), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c',
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_emoji(status_ser):

    sg.theme('DarkBlue2')

    entradas = [
        [sg.Text('Matricula:', font=font_input)],
        [sg.Input(key='-mat_emo-', justification='c',font=font_input,
        size=(20,1),enable_events=True),
        sg.Image('',key='-img_mat_emo-')],

        [sg.Text('Link Feliz:', font=font_input)],
        [sg.Input(key='-sta_link_f-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-status_f-')],

        [sg.Text('Link Cansado:', font=font_input)],
        [sg.Input(key='-sta_link_can-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-status_can-')],

        [sg.Text('Link Concentrado:', font=font_input)],
        [sg.Input(key='-sta_link_con-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-status_con-')],

        [sg.Text('Link Pensativo:', font=font_input)],
        [sg.Input(key='-sta_link_p-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-status_p-')],

        [sg.Text('Link Sério:', font=font_input)],
        [sg.Input(key='-sta_link_se-', justification='c',font=font_input,size=(20,1)),
        sg.Image('',key='-status_se-')],

    ]

    botoes = [
        [sg.B('Aplicar', font=font_login,size=(7,1),pad=(10,10)),
        sg.B('Ajuda',font=font_login,size=(7,1),pad=(10,10)),
        sg.B('Voltar', font=font_login, size=(7,1),pad=(10,10))]

    ]

    janela = [

        [sg.Column(layout= entradas)],

        [sg.Text('',key='-info_emoji-', font=font_input)],

        [sg.Column(layout=botoes)],

        [sg.Image(status_ser,key='-img_status_esq-')]

    ]

    return sg.Window('Emoji', finalize=True, size=(300,460), layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c',
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))


def tela_popup(tamanho,info,tipo_button,nome_janela ,entra_info=False,texto_entrada='',senha=''):
    sg.theme('DarkBlue2')
    
    info_txt = [
        [sg.Text(info,font=font_input)]
    ]

    if entra_info == True:
        entrada = [
            [sg.Text(texto_entrada, font=font_input)],
            [sg.Input(key='-entrada_padrao-',size=(20,1),password_char=senha,
            justification='c',enable_events=True)]
            ]

        voltar =[
            [sg.Button('Voltar',size=(7,1), font=font_input)]
            ]
    
    else:
        entrada = ''
        voltar = ''

    button = [
        [sg.Button(tipo_button,size=(7,1),font=font_input)]
        ]

    janela = [

        [sg.Column(layout=info_txt)],

        [sg.Column(layout=entrada)],

        [sg.Column(layout=button),sg.Column(layout=voltar)]
    ]

    return sg.Window(nome_janela, finalize=True, size=tamanho, layout = janela,
    margins=(0,0), element_justification='c', icon= (r'img\icon\ico_p.ico'),
    text_justification='c',modal=True,
    location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))