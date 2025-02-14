from tkinter import *
from tkinter.messagebox import askyesno,showerror,showinfo,showwarning
from config import *
from tkcalendar import Calendar
from datetime import datetime,timedelta
import requests 
import json
import os 

class Agenda:
    def __init__(self,root,titulo):
        self.root  = root 
        self.root.title(titulo)
        self.frame_principal_agenda = Frame(self.root,width=900,height=700,bg=cinza_elefante)
        self.frame_principal_agenda.pack()
        self.ano_atual = datetime.today().year
        self.mes_atual = datetime.today().month
        self.div_menu_lateral = LabelFrame(self.root,width=220,height=700)
        self.div_menu_lateral.place(x=10,y=2)

        self.div_lembrete = LabelFrame(self.frame_principal_agenda,width=420,height=220,bd=1,bg=cinza_elefante)
        
        self.renderizar_calendario()
        self.renderizar_lembrete()

        self.lembretes = self.carregar_lembretes()
        self.exibir_lembretes()

        self.verificar_lembretes() #Esse método inicia a verificação dos lembretes em segundo plano


    def renderizar_calendario(self):
        self.calendario = Calendar(self.frame_principal_agenda,selectmode="day",locale="pt_BR",date_pattern = "dd/MM/yyyy",font=("Arial",30),cursor="hand2")
        self.calendario.place(x=85,y=10)
        self.dia_hoje = datetime.today().strftime("%d/%m/%Y")
        self.calendario.selection_set(self.dia_hoje)
     
        Label(self.root,text=f"Hoje é {self.dia_hoje}",font="Verdana 12 bold",bg=cinza_elefante,fg=branco_padrao).place(x=610,y=20)
        

        self.botao_adicionar_lembrete = Button(self.div_menu_lateral,text="Adicionar Lembrete",font="arialblack 12 bold",bg='#ADD8E6',fg='black',cursor='hand2',command=self.adicionar_lembrete)
        self.botao_adicionar_lembrete.place(x=10,y=40,width=200)
        self.botao_adicionar_lembrete.bind("<Enter>",lambda event: self.botao_adicionar_lembrete.config(bg="#6a8891",fg="white"))
        self.botao_adicionar_lembrete.bind("<Leave>",lambda event: self.botao_adicionar_lembrete.config(bg="#ADD8E6",fg="black"))
        self.botao_retornar = Button(self.div_menu_lateral,text="Voltar ao menu principal",font="arial 12 bold",cursor="hand2",bg="#ADD8E6",fg="black",command=self.voltar_menu_principal)
        self.botao_retornar.place(x=10,y=1)
        self.botao_retornar.bind("<Enter>",lambda event: self.botao_retornar.config(bg="#6a8891",fg="white"))
        self.botao_retornar.bind("<Leave>",lambda event: self.botao_retornar.config(bg="#ADD8E6",fg="black"))


        self.div_feriados = LabelFrame(self.frame_principal_agenda,width=300,height=200,bd=1,bg=cinza_elefante)
        self.div_feriados.place(x=88,y=450)

        
        self.div_lembrete.place(x=400,y=450)

        

        self.titulo_feriado = Label(self.div_feriados,text='')
        self.label_feriado = Label(self.div_feriados, text='', font="Verdana 14", bg=cinza_elefante, fg="white",
                                   justify=LEFT, wraplength=400)
        self.label_feriado.place(x=5, y=5)
        self.detectar_mes()
        self.listar_feriados_mes()  # Chama a função para exibir os feriados do mês inteiro
    def renderizar_lembrete(self):
        self.label_titulo_lembrete = Label(self.div_lembrete,text="Lembretes",font="arialblack 14 bold",fg='white',bg=cinza_elefante)
        self.label_titulo_lembrete.place(x=140,y=2)
    
    def adicionar_lembrete(self):
        self.data_selecionada = self.calendario.get_date()

        def salvar():
            
            texto = entrada_texto.get("1.0",END).strip()
            horario = entrada_hora.get().strip()

            if texto and horario:
                try:
                    datetime.strptime(horario,"%H:%M") 

                    if self.data_selecionada not in self.lembretes:
                        self.lembretes[self.data_selecionada] = []
                    
                    self.lembretes[self.data_selecionada].append({"hora":horario,"texto":texto})
                    self.salvar_lembretes()
                    showinfo("Sucesso!","Lembrete salvo com sucesso!")
                    janela.destroy()
                    self.exibir_lembretes()

                    

                except ValueError:
                    showerror("ERROR","Formato de hora inválido")

        janela = Toplevel(self.root)
        janela.title("Novo Lembrete")
        janela.geometry("300x250")
        janela.resizable(0,0)
        Label(janela,text=f"Lembrete para {self.data_selecionada}:",font=("arial",12)).pack(pady=5)

        Label(janela,text="Horário (HH:MM):",font=("Arial",10)).pack()
        entrada_hora = Entry(janela,width=10)
        entrada_hora.pack()

        entrada_texto = Text(janela,height=5,width=30)
        entrada_texto.pack()

        Button(janela,text="Salvar",command=salvar,bg="lightgreen",cursor="hand2").pack(pady=5)



    def exibir_lembretes(self):
    # Limpa os widgets anteriores
        for widget in self.div_lembrete.winfo_children():
            widget.destroy()

    # Criando um container dentro da div_lembrete para organizar os lembretes
        self.container_lembretes = Frame(self.div_lembrete, bg=cinza_elefante)
        self.container_lembretes.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Título fixo dentro da div_lembrete
        self.label_titulo_lembrete = Label(
        self.container_lembretes, text="Lembretes", font="arialblack 14 bold",
        fg='white', bg=cinza_elefante
    )
        self.label_titulo_lembrete.pack(pady=5)

        self.data_selecionada = self.calendario.get_date()
        lembretes_do_dia = self.lembretes.get(self.data_selecionada, [])

        if lembretes_do_dia:
            for idx, lembrete in enumerate(lembretes_do_dia):
                frame_lembrete = Frame(self.container_lembretes, bg="yellow", padx=10, pady=5)
                frame_lembrete.pack(fill="both", padx=5, pady=2)

                label_texto = Label(
                frame_lembrete,
                text=f"{lembrete['hora']} - {lembrete['texto']}",
                font=("Arial", 10),
                bg="yellow",
                wraplength=300
            )
                label_texto.pack(side=LEFT, padx=5)

                btn_excluir = Button(
                frame_lembrete,
                text="🗑 Excluir",
                font=("Arial", 9, "bold"),
                bg="red",
                fg="white",
                cursor="hand2",
                command=lambda i=idx: self.excluir_lembrete(i)
            )
                btn_excluir.pack(side=RIGHT, padx=5)

        else:
            Label(
            self.container_lembretes,
            text="Nenhum lembrete para este dia",
            font=("Arial", 10),
            bg=cinza_elefante,
            fg="white"
        ).pack(pady=5)


    def excluir_lembrete(self, indice):
        if askyesno("Confirmação", "Tem certeza que deseja excluir este lembrete?"):
            self.lembretes[self.data_selecionada].pop(indice)

        # Se não houver mais lembretes na data, remove a chave do dicionário
        if not self.lembretes[self.data_selecionada]:
            del self.lembretes[self.data_selecionada]

        self.salvar_lembretes()
        self.exibir_lembretes()  # Atualiza a tela

    def salvar_lembretes(self):
        with open("lembretes.json","w") as arquivo:
            json.dump(self.lembretes,arquivo)
    
    def carregar_lembretes(self):
        if os.path.exists("lembretes.json"):
            try:
              with open("lembretes.json", "r") as arquivo:
                   return json.load(arquivo)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}  # Retorna um dicionário vazio caso ocorra erro
        return {}


    def verificar_lembretes(self):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        data_atual = datetime.now().strftime("%d/%m/%Y")
        hora_atual = datetime.now().strftime("%H:%M")

        if data_atual in self.lembretes:
            for lembrete in self.lembretes[data_atual]:  # Corrigido "self.lembrete" para "self.lembretes"
                if lembrete["hora"] == hora_atual:
                 self.notificar_usuario(lembrete["texto"])

        self.root.after(60000, self.verificar_lembretes)
    
    def notificar_usuario(self,mensagem):
        alerta = Toplevel(self.root)
        alerta.title("Lembrete!")
        alerta.resizable(0,0)
        Label(alerta, text="🔔 Lembrete!", font=("Arial", 14, "bold")).pack(pady=10)
        Label(alerta, text=mensagem, font=("Arial", 12), wraplength=280).pack(pady=5)
        Button(alerta, text="OK", command=alerta.destroy, bg="red", fg="white").pack(pady=10)

    def voltar_menu_principal(self):
        from menu_principal import MenuPrincipal 
        self.menu_principal = MenuPrincipal(self.root)
        self.frame_principal_agenda.pack_forget()
        self.botao_retornar.destroy()
        self.botao_adicionar_lembrete.destroy()

    def detectar_mes(self):
        self.meses = ['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']

        if self.mes_atual == 1:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[0]}"
        
        elif self.mes_atual == 2:
           self.label_feriado['text'] = f"FERIADOS DE {self.meses[1]}"
        elif self.mes_atual == 3:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[2]}"
        
        elif self.mes_atual == 4:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[3]}"
        
        elif self.mes_atual == 5:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[4]}"
        elif self.mes_atual == 6:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[5]}"
        
        elif self.mes_atual == 7:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[6]}"
        
        elif self.mes_atual == 8:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[7]}"
        
        elif self.mes_atual == 9:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[8]}"
        
        elif self.mes_atual == 10:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[9]}"
        elif self.mes_atual == 11:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[10]}"
        
        elif self.mes_atual == 12:
            self.label_feriado['text'] = f"FERIADOS DE {self.meses[11]}"

    def listar_feriados_mes(self):
        

        try:
            response = requests.get(f'https://api.invertexto.com/v1/holidays/{self.ano_atual}?token={token}')
            response.raise_for_status()
            feriados = response.json()
        except requests.exceptions.RequestException as e:
            self.label_feriado['text'] = "Erro ao buscar feriados"
            print(f"Erro na requisição: {e}")
            return

        # Filtra os feriados que pertencem ao mês atual
        feriados_do_mes = [f"{feriado['date']}: {feriado['name']}" for feriado in feriados
                           if int(feriado['date'][5:7]) == self.mes_atual]

        if feriados_do_mes:
            self.label_feriado['text'] = "Feriados deste mês:\n" + "\n".join(feriados_do_mes)
        else:
            self.label_feriado['text'] = "Nenhum feriado neste mês"
