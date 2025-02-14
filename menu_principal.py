from tkinter import *
from tkinter.messagebox import showerror, askyesno, showinfo
from config import *
from tkinter import PhotoImage
import os



class MenuPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz 

        self.divPrincipal = Frame(self.raiz, width=largura_div_principal, height=altura_div_principal, bd=1, bg=cinza_elefante)
        self.div_secundaria = Frame(self.divPrincipal, width=largura_div_secundaria, height=altura_div_secundaria, bd=1, bg=cinza_elefante)
        self.div_orcamento = Frame(self.divPrincipal, width=largura_div_secundaria, height=altura_div_secundaria, bd=1, bg=cinza_elefante)

        self.div_botao1 = LabelFrame(self.div_secundaria, width=largura_div_botoes, height=altura_div_botoes, bd=0, bg=cinza_elefante)
        self.div_botao2 = LabelFrame(self.div_secundaria, width=largura_div_botoes, height=altura_div_botoes, bd=0, bg=cinza_elefante)
        self.div_botao_orcamento = LabelFrame(self.div_secundaria, width=largura_div_botoes, height=altura_div_botoes, bd=1, bg=cinza_elefante)
        

        self.renderizar_divs()
        

    def renderizar_icones(self, imagem_pasta, arquivo_nome):
        caminho_arquivo_icone = os.path.join(imagem_pasta, arquivo_nome)

        if not os.path.exists(caminho_arquivo_icone):
            showerror("Atenção", f"O arquivo {caminho_arquivo_icone} não foi encontrado!")
            return None
        return PhotoImage(file=caminho_arquivo_icone)

    def renderizar_divs(self):
        self.divPrincipal.pack()
        self.div_secundaria.place(x=3, y=100)
        self.div_botao1.place(x=3, y=50)
        self.div_botao2.place(x=347, y=50)
        self.div_botao_orcamento.place(x=690,y=50)

        self.label_titulo = Label(self.divPrincipal, text="NeoNote", font="Arialblack 40", bg=cinza_elefante, fg="white")
        self.label_titulo.place(x=350, y=2)

        self.icone_agenda = self.renderizar_icones("icones", "agenda.png") 
        self.icone_anotacao = self.renderizar_icones("icones", "anotacao_icone.png")
        self.icone_orcamento = self.renderizar_icones("icones","orcamento.png")

        self.label_agenda = Label(self.div_secundaria, text="Agenda", font="Arialblack 18 bold", fg=branco_padrao, bg=cinza_elefante)
        self.label_agenda.place(x=100, y=10)
        self.label_anotacao = Label(self.div_secundaria, text="Anotação", font="Arialblack 18 bold", fg=branco_padrao, bg=cinza_elefante)
        self.label_anotacao.place(x=430, y=10)
        self.label_orcamento = Label(self.div_secundaria, text="Orçamento", font="Arialblack 18 bold", fg=branco_padrao, bg=cinza_elefante)
        self.label_orcamento.place(x=770, y=10)
        
        self.btn_agenda = Button(self.div_botao1, image=self.icone_agenda, width=298, height=264, cursor="hand2",command=self.ir_para_agenda)
        self.btn_agenda.place(x=1, y=1)
        self.btn_agenda.bind("<Enter>",lambda event:self.btn_agenda.config(bg=azul_escuro))
        self.btn_agenda.bind("<Leave>",lambda event:self.btn_agenda.config(bg=branco_padrao))

        self.btn_anotacao = Button(self.div_botao2, image=self.icone_anotacao, width=298, height=264, bd=0, cursor="hand2", command=self.renderizar_frame_anotacao)
        self.btn_anotacao.place(x=1, y=1)

        self.btn_anotacao.bind("<Enter>",lambda event:self.btn_anotacao.config(bg=azul_escuro))
        self.btn_anotacao.bind("<Leave>",lambda event:self.btn_anotacao.config(bg=branco_padrao))

        self.btn_orcamento = Button(self.div_botao_orcamento, image=self.icone_orcamento, width=298, height=264, bd=0, cursor="hand2",command=self.renderizar_frame_orcamento)
        self.btn_orcamento.place(x=1, y=1)
        self.btn_orcamento.bind("<Enter>",lambda event:self.btn_orcamento.config(bg=azul_escuro))
        self.btn_orcamento.bind("<Leave>",lambda event:self.btn_orcamento.config(bg=branco_padrao))

    def ir_para_agenda(self):
        from agenda import Agenda
        self.divPrincipal.destroy() 
        self.agenda_instance = Agenda(self.raiz,titulo_agenda)

    def renderizar_frame_anotacao(self):
        """Transição para o caderno"""
        from caderno import NeoNote
        self.divPrincipal.destroy()  # Remove o menu principal antes de abrir o caderno
        self.caderno_instancia = NeoNote(self.raiz)

    def renderizar_frame_orcamento(self):
        from orcamento import Orcamento
        self.divPrincipal.destroy()
        self.orcamento_instance = Orcamento(self.raiz,titulo_orcamento)