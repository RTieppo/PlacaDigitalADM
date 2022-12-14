import mysql.connector
from mysql.connector import Error

class BancoDeDados:
    def __init__(self,host,user, database, password):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
    
    def conecta(self):
        global conex
        try:
            conex = mysql.connector.connect(host = self.host ,user = self.user,
            database = self.database, password = self.password)

            if conex.is_connected():
                return True

            else:
                return False

        except Error as erro:
            return erro

    def reconecta(self):
        try:

            if conex.is_connected():
                return (True, 'tava')
            
            else:
                conex.connect()

                if conex.is_connected():
                    return (True,'volto')
        
        except Error:
            return False

    def consulta_conex(self):

        try:
            if conex.is_connected():
                return True
            
            else:
                return False
                
        except Error:
            return False
        
    def consulta_user(self,user_id):

        try:
            if conex.is_connected():
                info = ('select id from login;')
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()

                for linha in linhas:
                    if user_id == linha[0]:
                        return (True, user_id)
                else:
                    return (False,None)
            
            else:
                return(False,None)

        except Error as error:
            print(error)
            return ('Error ID',None)

    def consulta_senha(self,user_id):

        try:
            if conex.is_connected():

                info = (f"select senha from login where id = '{user_id}';")
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchone()
                
                return (str(linhas[0]))

        except Error:
            return 'Error Senha'

    def consulta_matricula(self, matricula):
        
        try:
            if conex.is_connected():

                info = ('select matricula from login order by id;')
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()
                
                for linha in linhas:
                    for le in linha:
                        converte = str(le)

                        if converte == matricula:
                            return True
                    
                else:
                    return False

        except Error:
            return 'Error matricula'


    def altera_senha(self,n_senha,matricula):
        try:
           
           if conex.is_connected():

                alterador = (f"update login set senha='{n_senha}' where matricula='{matricula}';")
                cursor = conex.cursor()
                cursor.execute(alterador)
                conex.commit()
                return True

        except Error:
            return 'Erro altera????o senha'


    def add_novo_user(self,Nmat,Nid):
        try:

            if conex.is_connected():
                novo_user = (f"""
                insert into login
                (matricula,id,senha)
                values
                ('{Nmat}','{Nid}',default);""")
                cursor = conex.cursor()
                cursor.execute(novo_user)
                conex.commit()
                return True
            
            else:
                return False

        except Error:
            return 'Erro ao cadastrar'
    
    def add_novos_emoji(self,matricula,feliz,cansado,concentrado,pensativo,serio):
        try:

            if conex.is_connected():
                novos_emoji = (f"""
                insert into emoji
                (matricula,link_fe,link_ca,link_co,link_pe,link_se)
                values
                ('{matricula}','{feliz}','{cansado}','{concentrado}','{pensativo}','{serio}');""")
                cursor = conex.cursor()
                cursor.execute(novos_emoji)
                conex.commit()
                return True
            
            else:
                return False

        
        except Error:
            return 'Erro no cadastro'

    def add_info_primaria_status(self,matricula,hora):
        try:

            if conex.is_connected():

                novo_user = (f"""
                insert into status_atendimento
                (matricula,horario)
                values
                ('{matricula}','{hora}');
                """)
                cursor = conex.cursor()
                cursor.execute(novo_user)
                conex.commit()
                return True
            
            else:
                return False
        
        except Error:
            return'Erro no cadastro'
    
    def deleta_info_primaria(self,matricula):
        try:
            if conex.is_connected():

                deleta = (f"""
                delete from status_atendimento
                where matricula = '{matricula}';
                """)

                cursor = conex.cursor()
                cursor.execute(deleta)
                conex.commit()
                return True
            
            else:
                return False

        except Error:
            return 'Erro ao deletar'

    def add_info(self,titulo,texto):
        try:
            
            if conex.is_connected():
                
                add_info = (f"""
                insert into avisos
                (titulo,texto)
                values
                ('{titulo}','{texto}');
                """)

                cursor = conex.cursor()
                cursor.execute(add_info)
                conex.commit()

                return True

            else:
                return False

        except Error:
            return 'Erro ao aplicar info'


    def delata_novo_user(self,matricula):
        try:

            if conex.is_connected():

                deleta = (f"""
                delete from login
                where matricula = '{matricula}';
                """)

                cursor = conex.cursor()
                cursor.execute(deleta)
                conex.commit()
                return True
            
            else:
                return False

        except Error:
            return 'Erro ao deletar'

    def atualiza_emoji(self,matricula,feliz,cansado,concentrado,pensativo,serio):
        try:

            if conex.is_connected():
                novos_emoji = (f"""
                update emoji
                set link_fe = '{feliz}', link_ca = '{cansado}',
                link_co = '{concentrado}', link_pe = '{pensativo}', link_se = '{serio}'
                where matricula = '{matricula}';
                """)
                cursor = conex.cursor()
                cursor.execute(novos_emoji)
                conex.commit()
                return True
            
            else:
                return False

        except Error:
            return 'Erro no cadastro'

    def atualiza_status(self,matricula,status_agora,unidade,local_ss,humor):
        try:

            if conex.is_connected():
                atualiza_status =(f"""
                update status_atendimento
                set status_agora = '{status_agora}', unidade ='{unidade}',
                local_ss = '{local_ss}', humor = '{humor}'
                where matricula = '{matricula}';
                """)
                cursor = conex.cursor()
                cursor.execute(atualiza_status)
                conex.commit()
                return True
            
            else:
                return False


        except Error as erro:
            print(erro)
            return 'Erro na atualiza????o'
    
    def atualiza_status_sem_humor(self,matricula,status_agora,unidade,local_ss):
        try:

            if conex.is_connected():
                atualiza_status =(f"""
                update status_atendimento
                set status_agora = '{status_agora}', unidade ='{unidade}',
                local_ss = '{local_ss}'
                where matricula = '{matricula}';
                """)
                cursor = conex.cursor()
                cursor.execute(atualiza_status)
                conex.commit()
                return True
            
            else:
                return False


        except Error:
            return 'Erro na atualiza????o'

    def coleta_matricula(self,user):
        try:
            if conex.is_connected():
                info = (f"select matricula from login where id='{user}';")
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()
                return linhas[0][0]
        
        except Error:
            return 'erro_nv_acesso'

    def coleta_link(self,matricula):
        try:
            if conex.is_connected():
                info = (f"select * from emoji where matricula='{matricula}';")
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()

                dados_link = list()

                for num in linhas:
                    for separa in num:
                        converte = str(separa)
                        if len(converte) > 8:
                            dados_link.append(converte)
                        
                    return dados_link
                        
        except Error:
            return 'erro_coleta_de_links'

    def verifica_duplicata(self,new_id):
        try:
            
            if conex.is_connected():
                info = ('select matricula from login;')
                cursor = conex.cursor()
                cursor.execute(info)
                linhas = cursor.fetchall()

                for linha in linhas:
                    formata = str(linha[0])

                    if formata in new_id:
                        return False

                else:
                    return True

        except Error:
            return 'Error verifica????o'