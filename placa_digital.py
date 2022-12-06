from PySimpleGUI import PySimpleGUI as sg
from time import sleep

from bib_extra import telas as t
from bib_extra import txt_fun as txt
from bib_extra import slq_fun as sql
from bib_extra import analise_dados as dados
import DadosBancoDeDados as d


def start_serve():
    global test_conex

    test_conex = sql.BancoDeDados(host=d.host,user=d.user, database=d.database,
        password=d.password)       

    retorno = test_conex.conecta()

    if retorno[0] == True:
        abre_txt = txt.le_txt()
        
        if abre_txt[1] == True:
            if len(abre_txt) > 1:
                return (t.tela_login(user_login = abre_txt[0][0],
                status=retorno[1], memoria=abre_txt[0][1]))
            
            else:
                return (t.tela_login(user_login = '',
                status= retorno[1], memoria=''))

        else:
            return (t.tela_login(user_login = '', status= retorno[1],
            memoria=''))


def roda_app(star):
    global test_conex

    janela_login = star

    janela_adm = janela_esqueci = janela_novo_user = None

    limitador_info_atendimento = 0
    
    id_ref = ''
    apelido = ''
    matri = ''

    erro = (r'img\20_20\erro.png')
    verificado = (r'img\20_20\verificado.png')
    icone = (r'img\icon\ico_p.ico')
    
    while True:

        window, eventos, valores = sg.read_all_windows()

        if window == janela_login and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_login and eventos == 'Entrar':
            sg.user_settings_set_entry('-last position-', janela_login.current_location())
            window['-info_user-'].update('')

            retorno_test = test_conex.consulta_conex()

            if retorno_test == True:

                retorno_user = test_conex.consulta_user(user_id = valores['-user-'])

                if retorno_user == 'Error ID':
                    window['-img_status-'].update(r'img\20_20\erro.png')

                elif retorno_user[0] == True:

                    retorno_senha = test_conex.consulta_senha(user_id = retorno_user[1])

                    if retorno_senha == 'Error Senha':
                        window['-img_status-'].update(erro)

                    elif retorno_senha == valores['-senha-']:
                        retorno_senha = True

                        if retorno_user and retorno_senha == True:

                            window['-img_v_user-'].update(verificado)
                            window['-img_v_senha-'].update(verificado)

                            if valores['-save-'] == True:
                                txt.cria_pasta() 
                                txt.cria_txt(valores['-user-'])
                            
                            elif valores['-save-'] == False:
                                txt.limpa_txt()

                            apelido = test_conex.consulta_apelido(id_user = valores['-user-'])
                            id_ref = retorno_user[1]
                            matri = test_conex.coleta_matricula(id_ref)
                            nv_acesso = test_conex.coleta_acesso(id_ref)

                            window['-info_user-'].update('Usuário valido',None,'darkgreen')
                            window.refresh()
                            sleep(1)
                            window['-info_user-'].update('Acessando...',None,'darkgreen')
                            window.refresh()
                            sleep(1)

                            janela_login.close()
                            janela_adm = t.tela_adm(apelido_user=apelido)
                            #colocar tratamento para erro de coleta de informações
                    
                    elif retorno_user[0] or retorno_senha == True:

                        if retorno_senha != True:
                            window['-img_v_senha-'].update(erro)

                        if retorno_user[0] == True:
                            window['-img_v_user-'].update(verificado)
                    
                    else:
                        window['-img_v_senha-'].update(erro)

                elif retorno_user[0] == False:
                    window['-img_v_user-'].update(erro)
            
            else:
                window['-img_status-'].update(erro)

        elif window == janela_login and eventos == 'Esqueci':
            sg.user_settings_set_entry('-last position-', janela_login.current_location())

            retorno = test_conex.consulta_conex()

            if retorno == True:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(verificado)
            
            else:
                janela_login.hide()
                janela_esqueci = t.tela_esqueci(erro)

    #Janela esqueci senha

        if window == janela_esqueci and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_esqueci and eventos == 'Voltar':
            sg.user_settings_set_entry('-last position-', janela_esqueci.current_location())
            janela_esqueci.close()
            janela_login.un_hide()

        elif window == janela_esqueci and eventos == 'Alterar':

            window['-info_user_es-'].update('')
            window['-img_v_mat-'].update('')
            window['-img_v_ns-'].update('')
            window['-img_c_ns-'].update('')

            validaDados = dados.ValidaDados(matricula=valores['-mat-'],
            senha=(valores['-senhaN1-'],valores['-senhaN2-']))

            resultadoSenha = validaDados.valida_senha()
            resultadoMatricula = validaDados.valida_matricula()

            if resultadoMatricula == True:
                consulta = test_conex.consulta_matricula(matricula=valores['-mat-'])

                if consulta == True:
                    window['-img_v_mat-'].update(verificado)
                
                elif consulta == 'Error matricula':
                    window['-img_status_esq-'].update(erro)
                
                else:
                    window['-img_v_mat-'].update(erro)
            else:
                window['-img_v_mat-'].update(erro)
            

            if resultadoSenha[0] == False:
                window['-img_v_ns-'].update(erro)
            
            if resultadoSenha[1] == False:
                window['-img_c_ns-'].update(erro)
            
            if resultadoSenha[0] == True and resultadoSenha[1] == True and resultadoMatricula == True:

                if valores['-senhaN1-'] == valores['-senhaN2-']:
                    window['-img_v_ns-'].update(verificado)
                    window['-img_c_ns-'].update(verificado)

                    window['-info_user_es-'].update('Dados validos!', None,'darkgreen')

                    window.refresh()
                    sleep(1)

                    window['-info_user_es-'].update('Atualizando!', None,'darkgreen')
                    altera_senha = test_conex.altera_senha(n_senha=valores['-senhaN1-'],
                    matricula=valores['-mat-'])

                    window.refresh()
                    sleep(1)

                    if altera_senha == True:
                        window['-info_user_es-'].update('Senha alterada!', None,'darkgreen')
                    
                    elif altera_senha == 'Erro alteração senha':
                        window['-img_status_esq-'].update(erro)
                    
                    else:
                        window['-info_user_es-'].update('Erro na alteração!', None,'darkred')
                
                else:
                    window['-img_v_ns-'].update(erro)
                    window['-img_c_ns-'].update(erro)

        elif window == janela_esqueci and eventos == 'Ajuda':
            sg.user_settings_set_entry('-last position-', janela_esqueci.current_location())

            sg.popup_no_buttons(open(r'ark_txt\ajuda_esqueci.txt','r', encoding='utf-8').read(),
            title='Redefinição de senha',
            location=tuple(sg.user_settings_get_entry('-last position-', (None, None))),
            icon= icone
            ) 
    
    #janela adm menu
        elif window == janela_adm and eventos == 'About':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())
            sg.popup('Duvidas contate o administrador:\nGitHub: Rtieppo\nRamal: 3271',
            title='Ajuda!',icon= icone,
            location=tuple(sg.user_settings_get_entry('-last position-', (None, None))),
            )

        elif window == janela_adm and eventos == 'ID':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())
            novo_id_user = sg.popup_get_text(
                'O novo ID deve conter até 10 caracteres.\nNovo ID:',
                title='Novo ID', icon=icone,size=(25,25),
                location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
            )

            if novo_id_user != None:

                if len(novo_id_user) <= 10 and len(novo_id_user) > 0:
                    troca_id = test_conex.altera_id_user(matricula=matri,nv_id=novo_id_user)

                    if troca_id == True:

                        sg.popup_ok(
                            'ID alterado com sucesso!', title='Alterado', icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                        )
                    
                    else:
                        sg.popup_error(
                            'Erro na troca do ID',title='Error',icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                        )
                
                else:
                    sg.popup_ok(
                        'ID invalido, fora do padrão\nTente novamente...', title='Error',
                        icon= icone,
                        location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                    )

        elif window == janela_adm and eventos =='Senha':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())
            nova_senha = sg.popup_get_text(
                'A senha deve ser númerica e conter\n4 caracteres.\nNova Senha:',
                title= 'Nova senha',icon=icone,password_char='*', size=(25,25),
                location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                )
            
            if nova_senha != None:

                if nova_senha.isnumeric() and len(nova_senha)==4:
                    troca_senha = test_conex.altera_senha(matricula=matri, n_senha=nova_senha)

                    if troca_senha == True:

                        sg.popup_ok(
                            'Senha alterada com sucesso!',title='Alterado',icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                        )

                    else:
                        sg.popup_error(
                            'Erro na troca da senha!',title='Error',icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                        )

                else:
                    sg.popup_ok(
                        'Senha informada é invalida\nTente novamente...',title='Error',
                        icon= icone,
                        location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                    )

        elif window == janela_adm and eventos == 'Apelido':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())
            novo_apelido = sg.popup_get_text(
                'O Novo apelido deve conter até 10 caracteres.\nNovo Apelido:',
                title='Novo Apelido', icon=icone, size=(25,25),
                location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
            )

            if novo_apelido != None:
                
                if len(novo_apelido) <= 10 and len(novo_apelido) > 0:
                    troca_apelido = test_conex.altera_apelido(matricula=matri,nv_apel=novo_apelido)

                    if troca_apelido == True:

                        sg.popup_ok(
                            'Apelido alterado com sucesso!', title='Alterado', icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))

                        )
                    
                    else:
                        sg.popup_error(
                            'Erro na troca do apelido', title='Error', icon=icone,
                            location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                        )


                else:
                    sg.popup_ok(
                        'Apelido, fora ddo padrão\nTente novamente...', title='Error',
                        icon=icone,
                        location=tuple(sg.user_settings_get_entry('-last position-', (None, None)))
                    )

        elif window == janela_adm and eventos =='Novo user':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())

            consultaConex = test_conex.consulta_conex()

            if consultaConex == True:
                janela_adm.hide()
                janela_novo_user = t.tela_novo_user(verificado)

            else:
                janela_adm.hide()
                janela_novo_user = t.tela_novo_user(erro)
    
    #janela novo user

        if window == janela_novo_user and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_novo_user and eventos == 'Voltar':
            janela_adm.un_hide()
            janela_novo_user.close()
        
        elif window == janela_novo_user and eventos == 'Aplicar':

            window['-info_n_ca-'].update('')
            window['-img_n_mat-'].update('')
            window['-img_N_nome-'].update('')
            window['-img_N_apeli-'].update('')
            window['-img_n_id-'].update('')

            listaValores = ('-n_mat-','-n_nome-','-N_apelido-','-n_id-')

            contadorDeValidação = 0

            for valor in listaValores:
                if valores[valor] != '':
                    
                    if valor == '-n_mat-':
                        inicia = dados.ValidaDados(matricula=valores['-n_mat-'])
                        verifica_caracteres = inicia.valida_matricula()

                        if verifica_caracteres == True:
                            verifica_disponibilidade = test_conex.verifica_duplicata(new_id = valores['-n_mat-'])
                           
                            if verifica_disponibilidade == True:
                                window['-img_n_mat-'].update(verificado)
                                contadorDeValidação +=1

                            elif verifica_disponibilidade == False:
                                window['-img_n_mat-'].update(erro)
                            
                            else:
                                window['-img_status_esq-'].update(erro)
                        
                        else:
                            window['-img_n_mat-'].update(erro)
                        
                    elif valor == '-n_nome-':
                        inicia = dados.ValidaDados(nome=valores['-n_nome-'])
                        verifica_nome = inicia.valida_nome()


                        if verifica_nome == True:
                            contadorDeValidação +=1
                            window['-img_N_nome-'].update(verificado)
                        
                        else:
                            window['-img_N_nome-'].update(erro)
                    
                    elif valor == '-N_apelido-':
                        inicia = dados.ValidaDados(apelido=valores['-N_apelido-'])
                        verifica_apelido = inicia.valida_apelido()


                        if verifica_apelido == True:
                            contadorDeValidação +=1
                            window['-img_N_apeli-'].update(verificado)
                        
                        else:
                            window['-img_N_apeli-'].update(erro)
                    
                    elif valor == '-n_id-':
                        inicia = dados.ValidaDados(id=valores['-n_id-'])
                        verifica_n_id = inicia.valida_novo_id()

                        if verifica_n_id == True:
                            contadorDeValidação +=1
                            window['-img_n_id-'].update(verificado)
                        
                        else:
                            window['-img_n_id-'].update(erro)

                else:
                    window['-info_n_ca-'].update('Preencha Todos os campos',None,'darkred')
                
            if contadorDeValidação == 4:
                window['-info_n_ca-'].update('Informações validas',None,'darkgreen')
                window.refresh()
                sleep(1)

                window['-info_n_ca-'].update('Atualizando...',None,'darkgreen')
                window.refresh()
                sleep(1)

                cadastra = test_conex.add_novo_user(Nmat=valores['-n_mat-'],
                Nnome=valores['-n_nome-'], Napelido=valores['-N_apelido-'],Nid=valores['-n_id-'])

                if cadastra == True:
                    window['-info_n_ca-'].update('Cadastrado com Sucesso!',None,'darkgreen')
                
                elif cadastra == 'Erro ao cadastrar':
                    window['-img_status_esq-'].update(erro)
                
                else:
                    window['-info_n_ca-'].update('Erro ao cadastrar!',None,'darkred')

        elif window == janela_novo_user and eventos == 'Ajuda':
            sg.user_settings_set_entry('-last position-', janela_novo_user.current_location())

            sg.popup_no_buttons(open(r'ark_txt\ajuda_novo_user.txt','r', encoding='utf-8').read(),
            title='Cadastro novo usuário',
            location=tuple(sg.user_settings_get_entry('-last position-', (None, None))),
            icon= icone
            )


    # janela adm
        if window == janela_adm and eventos == sg.WIN_CLOSED or janela_adm and eventos == 'Sair':
            break

        elif window == janela_adm and eventos == '-ST_A-':

            if limitador_info_atendimento == 0:
                limitador_info_atendimento =+1

                janela_adm.extend_layout(janela_adm['-Add-'],
                [[sg.Text('Unidade:'), sg.Radio('Faculdade','-UN-', key='-FC-'),
                sg.Radio('Saúde e Beleza','-UN-', key='-SS-')]])

                janela_adm.extend_layout(janela_adm['-Add-'],
                [[sg.Text('Sala ou Setor:'), sg.In(key='-local-', justification='c'
                , size=(25,0))]])
            
        elif window == janela_adm and eventos == '-ST_H-':
            feliz = valores['-ST_H-']
            if feliz == 5:

                
                window['-img_hu-'].update(r'img\100_100\Feliz_100.png')
                window['-hu_r-'].update('Feliz',None,'darkgreen')
            
            print(feliz)
            
inicia = start_serve()
roda_app(inicia)

