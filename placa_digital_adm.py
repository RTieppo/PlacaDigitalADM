from PySimpleGUI import PySimpleGUI as sg
from time import sleep
import cv2

from bib_extra import telas as t
from bib_extra import txt_fun as txt
from bib_extra import slq_fun as sql
from bib_extra import analise_dados as dados
from bib_extra import buscador_img as img
from bib_extra import criador_pasta as pasta
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
                pasta.cria_pasta_geral()
                return (t.tela_login(user_login = abre_txt[0][0],
                status=retorno[1], memoria=abre_txt[0][1]))
            
            else:
                pasta.cria_pasta_geral()
                return (t.tela_login(user_login = '',
                status= retorno[1], memoria=''))

        else:
            pasta.cria_pasta_geral()
            return (t.tela_login(user_login = '', status= retorno[1],
            memoria=''))


def roda_app(star):
    global test_conex

    janela_login = star

    janela_adm = janela_esqueci = janela_novo_user = janela_emoji = janela_popup = None
    id_ref = apelido = matri = ''

    salva_janela_referencia = valor_coletado = tamanho_atual = janela_ref_popup = None

    erro = (r'img\20_20\erro.png')
    verificado = (r'img\20_20\verificado.png')

    limitador_caracter = ('-senha-','-entrada_padrao-','-senhaN1-','-senhaN2-',
    '-n_mat-','-mat-','-mat_emo-')
    
    while True:

        window, eventos, valores = sg.read_all_windows()

        for limita in limitador_caracter:
            if eventos == limita and len(valores[limita])>4:
                window.Element(limita).update(valores[limita][:-1])


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
                            window['-info_user-'].update('Usuário valido',None,'darkgreen')
                            window.refresh()
                            sleep(1)
                            
                            window['-info_user-'].update('Atualizando dados...',None,'yellow')
                            window.refresh()

                            ajusta_apelido = str (retorno_user[1]).split('.')
                            apelido = str(ajusta_apelido[0]).capitalize()
                            id_ref = retorno_user[1]
                            matri = str(test_conex.coleta_matricula(id_ref))

                            verifica_pasta_u = img.verifica_pasta_user(matricula=matri)

                            if verifica_pasta_u == True:
                                coleta_link = test_conex.coleta_link(matricula=matri)
                                if coleta_link != None:
                                    img.baixa_img(link=coleta_link,mat=matri)
                            
                            else:
                                pasta.cria_pasta_user(matricula=matri)
                                coleta_link = test_conex.coleta_link(matricula=matri)
                                if coleta_link != None:
                                    img.baixa_img(link=coleta_link,mat=matri)
                            
                            verifica_pasta_temp_img = img.verifica_pasta_temp()

                            if verifica_pasta_temp_img == False:
                                pasta.cria_pasta_temp()


                            if valores['-save-'] == True:
                                txt.cria_txt(valores['-user-'])
                            
                            elif valores['-save-'] == False:
                                txt.limpa_txt()

                            
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

    #janela popup

        if window == janela_popup and eventos == sg.WIN_CLOSED or eventos == 'OK':
            salva_janela_referencia.un_hide()
            janela_popup.close()
        
        elif window == janela_popup and eventos == 'Voltar':
            salva_janela_referencia.un_hide()
            janela_popup.close()

        elif window == janela_popup and eventos == 'Aplicar':
            valor_coletado = valores['-entrada_padrao-']
            janela_popup.hide()

            if janela_ref_popup == 'Senha':

                if valor_coletado.isnumeric() and len(valor_coletado)==4:

                    troca_senha = test_conex.altera_senha(matricula=matri, n_senha=valor_coletado)

                    if troca_senha == True:

                        ajuste_x = (f'{tamanho_atual[0]/2}')
                        ajuste_y = (f'{tamanho_atual[1]/5}')
                        texto = 'Senha alterada com sucesso!'


                        janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
                        info=texto,tipo_button='OK',nome_janela='Alterado')

                        valor_coletado = None
                        janela_ref_popup = None

                    else:

                        ajuste_x = (f'{tamanho_atual[0]/2}')
                        ajuste_y = (f'{tamanho_atual[1]/5}')
                        texto = 'Erro na troca da senha!'

                        janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
                        info=texto,tipo_button='OK',nome_janela='Error')

                        valor_coletado = None
                        janela_ref_popup = None
                else:

                    ajuste_x = (f'{tamanho_atual[0]/2}')
                    ajuste_y = (f'{tamanho_atual[1]/3}')
                    texto = 'Senha informada é invalida\nTente novamente...'

                    janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
                    info=texto,tipo_button='Aplicar',nome_janela='Error',
                    entra_info=True, texto_entrada='Novo Senha:',senha='*')


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
            
            tamanho_atual = window.Size
            
            texto = open(r'ark_txt\ajuda_esqueci.txt','r', encoding='utf-8').read()
            janela_esqueci.hide()
            salva_janela_referencia = janela_esqueci

            janela_popup = t.tela_popup(tamanho=tamanho_atual,
            info=texto,tipo_button='OK',nome_janela='Ajuda senha')
    

    #janela adm menu
        elif window == janela_adm and eventos == 'About':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())

            tamanho_atual = window.Size

            ajuste_x = (f'{tamanho_atual[0]/2}')
            ajuste_y = (f'{tamanho_atual[1]/4}')
            texto = 'Duvidas? Contate\no administrador:\nGitHub: Rtieppo\nRamal: 3271'
            janela_adm.hide()
            salva_janela_referencia = janela_adm

            janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
            info=texto,tipo_button='OK',nome_janela='Ajuda')
         
        elif window == janela_adm and eventos =='Senha':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())
            tamanho_atual = window.Size

            ajuste_x = (f'{tamanho_atual[0]/2}')
            ajuste_y = (f'{tamanho_atual[1]/3}')
            texto = 'A senha deve ser númerica e\nconter 4 caracteres.'
            janela_adm.hide()
            janela_ref_popup = 'Senha'
            salva_janela_referencia = janela_adm

            janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
            info=texto,tipo_button='Aplicar', entra_info=True,
            texto_entrada='Novo Senha:',nome_janela='Novo Senha', senha='*')
        
        elif window == janela_adm and eventos =='Novo user':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())

            consultaConex = test_conex.consulta_conex()

            if consultaConex == True:

                janela_adm.hide()
                janela_novo_user = t.tela_novo_user(verificado)


            else:
                janela_adm.hide()
                janela_novo_user = t.tela_novo_user(erro)

        elif window == janela_adm and eventos == 'Emoji':
            sg.user_settings_set_entry('-last position-', janela_adm.current_location())

            consultaConex = test_conex.consulta_conex()

            if consultaConex == True:
                janela_adm.hide()
                janela_emoji = t.tela_emoji(verificado)
            
            else:
                janela_adm.hide()
                janela_emoji = t.tela_adm(erro)
                
    #janela emoji

        if window == janela_emoji and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_emoji and eventos == 'Voltar':
            sg.user_settings_set_entry('-last position-', janela_emoji.current_location())
            janela_emoji.close()
            janela_adm.un_hide()

        elif window == janela_emoji and eventos == 'Aplicar':
            window['-info_emoji-'].update('')

            verifica_valores = ('-mat_emo-','-sta_link_f-','-sta_link_can-',
            '-sta_link_con-','-sta_link_p-','-sta_link_se-')

            contador_links = 0
            status_atualiza_new = None

            for valor in verifica_valores:
                
                if valores[valor]!= '':

                    if valor == '-mat_emo-':
                        inicia = dados.ValidaDados(matricula=valores['-mat_emo-'])
                        valida_mat = inicia.valida_matricula()

                        if valida_mat == True:
                            contador_links += 1
                            window['-img_mat_emo-'].update(verificado)
                            verifica_existencia = test_conex.verifica_duplicata(new_id=valores['-mat_emo-'])

                            if verifica_existencia == True:
                                status_atualiza_new = '-new-'

                            else:
                                status_atualiza_new = '-atualiza-'

                        else:
                            window['-mat_emo-'].update(erro)

                    elif valor == '-sta_link_f-':
                        valida_link = dados.valida_link(valores['-sta_link_f-'])
                        
                        if valida_link == True:
                            window['-status_f-'].update(verificado)
                            contador_links += 1

                        else:
                            window['-status_f-'].update(erro)

                    elif valor == '-sta_link_can-':
                        valida_link = dados.valida_link(valores['-sta_link_can-'])
                        
                        if valida_link == True:
                            window['-status_can-'].update(verificado)
                            contador_links += 1

                        else:
                            window['-status_can-'].update(erro)

                    elif valor == '-sta_link_con-':
                        valida_link = dados.valida_link(valores['-sta_link_con-'])
                        
                        if valida_link == True:
                            window['-status_con-'].update(verificado)
                            contador_links += 1

                        else:
                            window['-status_con-'].update(erro)

                    elif valor == '-sta_link_p-':
                        valida_link = dados.valida_link(valores['-sta_link_p-'])
                        
                        if valida_link == True:
                            window['-status_p-'].update(verificado)
                            contador_links += 1

                        else:
                            window['-status_p-'].update(erro)

                    elif valor == '-sta_link_se-':
                        valida_link = dados.valida_link(valores['-sta_link_se-'])
                        
                        if valida_link == True:
                            window['-status_se-'].update(verificado)
                            contador_links += 1

                        else:
                            window['-status_se-'].update(erro)
                else:
                    window['-info_emoji-'].update('Preencha Todos os campos!',None,'darkred')
            
            if contador_links == 6:
                
                if status_atualiza_new == '-new-':

                    window['-info_emoji-'].update('Dados validos',None,'darkgreen')
                    window.refresh()
                    sleep(1)

                    window['-info_emoji-'].update('Gravando novo cadastro...',None,'darkgreen')
                    window.refresh()
                    sleep(1)

                    add_novo_cadastro = test_conex.add_novos_emoji(matricula=valores['-mat_emo-'],
                    feliz=valores['-sta_link_f-'],cansado=valores['-sta_link_can-'],
                    concentrado=valores['-sta_link_con-'],pensativo=valores['-sta_link_p-'],
                    serio=valores['-sta_link_se-'])


                    if add_novo_cadastro == True:
                        window['-info_emoji-'].update('Dados gravados',None,'darkgreen')
                        window.refresh()
                    
                    elif add_novo_cadastro == 'Erro no cadastro':
                        window['-img_status_esq-'].update(erro)
                    
                    else:
                        window['-info_emoji-'].update('Erro de cadastro',None,'darkred')

                else:
                    window['-info_emoji-'].update('Dados validos',None,'darkgreen')
                    window.refresh()
                    sleep(1)

                    window['-info_emoji-'].update('Atualizando cadastro...',None,'darkgreen')
                    window.refresh()
                    sleep(1)
                    
                    atualiza_cadastro_emoji = test_conex.atualiza_emoji(matricula=valores['-mat_emo-'],
                    feliz=valores['-sta_link_f-'],cansado=valores['-sta_link_can-'],
                    concentrado=valores['-sta_link_con-'],pensativo=valores['-sta_link_p-'],
                    serio=valores['-sta_link_se-'])

                    if atualiza_cadastro_emoji == True:
                        window['-info_emoji-'].update('Dados gravados',None,'darkgreen')
                        window.refresh()
                    
                    elif add_novo_cadastro == 'Erro no cadastro':
                        window['-img_status_esq-'].update(erro)
                    
                    else:
                        window['-info_emoji-'].update('Erro de cadastro',None,'darkred')

        elif window == janela_emoji and eventos == 'Ajuda':
            sg.user_settings_set_entry('-last position-', janela_emoji.current_location())

            tamanho_atual = window.Size

            ajuste_x = (f'{tamanho_atual[0]/1.1}')
            ajuste_y = (f'{tamanho_atual[1]/1.3}')

            texto = open(r'ark_txt\ajuda_links.txt','r', encoding='utf-8').read()
            janela_emoji.hide()
            salva_janela_referencia = janela_emoji

            janela_popup = t.tela_popup(tamanho=(ajuste_x[0:3],ajuste_y[0:3]),
            info=texto,tipo_button='OK',nome_janela='Ajuda emoji')


    #janela novo user

        if window == janela_novo_user and eventos == sg.WIN_CLOSED:
            break

        elif window == janela_novo_user and eventos == 'Voltar':
            janela_adm.un_hide()
            janela_novo_user.close()
        
        elif window == janela_novo_user and eventos == 'Aplicar':

            window['-info_n_ca-'].update('')
            window['-img_n_mat-'].update('')
            window['-img_n_id-'].update('')

            listaValores = ('-n_mat-','-n_id-')

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
                
            if contadorDeValidação == 2:
                window['-info_n_ca-'].update('Informações validas',None,'darkgreen')
                window.refresh()
                sleep(1)

                window['-info_n_ca-'].update('Atualizando...',None,'darkgreen')
                window.refresh()
                sleep(1)

                cadastra = test_conex.add_novo_user(Nmat=valores['-n_mat-'],
                Nid=valores['-n_id-'])

                if cadastra == True:
                    window['-info_n_ca-'].update('Cadastrado com Sucesso!',None,'darkgreen')
                
                elif cadastra == 'Erro ao cadastrar':
                    window['-img_status_esq-'].update(erro)
                
                else:
                    window['-info_n_ca-'].update('Erro ao cadastrar!',None,'darkred')

        elif window == janela_novo_user and eventos == 'Ajuda':
            sg.user_settings_set_entry('-last position-', janela_novo_user.current_location())

            tamanho_atual = window.Size

            texto = open(r'ark_txt\ajuda_novo_user.txt','r', encoding='utf-8').read()
            janela_novo_user.hide()

            salva_janela_referencia = janela_novo_user

            janela_popup = t.tela_popup(tamanho=tamanho_atual,
            info=texto,tipo_button='OK',nome_janela='Ajuda cadastro')


    # janela adm
        if window == janela_adm and eventos == sg.WIN_CLOSED or janela_adm and eventos == 'Sair':
            break
   
        elif window == janela_adm and eventos == '-ST_H-':

            valida_ark_img = img.verifica_ark_img(matricula=matri)

            if valida_ark_img == True:

                if valores['-ST_H-'] == 5:

                    ajuste = img.ajusta_img(matricula=matri,ark='feliz.png')

                    window['-img_hu-'].update(ajuste)
                    window['-hu_r-'].update('Feliz',None,'darkgreen')
                
                elif valores['-ST_H-'] == 4:

                    ajuste = img.ajusta_img(matricula=matri,ark='pensativo.png')

                    window['-img_hu-'].update(ajuste)
                    window['-hu_r-'].update('Pensativo',None,'darkgreen')
                    

                elif valores['-ST_H-'] == 3:
                    ajuste = img.ajusta_img(matricula=matri,ark='concentrado.png')

                    window['-img_hu-'].update(ajuste)
                    window['-hu_r-'].update('Concentrado',None,'darkgreen')

                elif valores['-ST_H-'] == 2:
                    ajuste = img.ajusta_img(matricula=matri,ark='cansado.png')

                    window['-img_hu-'].update(ajuste)
                    window['-hu_r-'].update('Cansado',None,'darkred')

                elif valores['-ST_H-'] == 1:
                    ajuste = img.ajusta_img(matricula=matri,ark='serio.png')

                    window['-img_hu-'].update(ajuste)
                    window['-hu_r-'].update('Serio',None,'darkred')
            
            else:
                window['-hu_r-'].update('imagens indisponíveis!',None,'darkred')
                
inicia = start_serve()
roda_app(inicia)

