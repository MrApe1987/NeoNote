from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from main import * 

class NeoNote:
    def __init__(self, root):
        self.root = root
        self.frame_caderno = Frame(self.root)
        self.frame_caderno.pack()
        # Criação da barra de menu
        self.barraMenu = Menu(self.root)
        self.root.config(menu=self.barraMenu)

        # Criação do menu 'Arquivo' com seus itens
        self.arquivo = Menu(self.barraMenu, tearoff=0)
        self.arquivo.add_command(label="Novo", command=self.novo)
        self.arquivo.add_command(label="Abrir", command=self.abrir)
        self.arquivo.add_command(label="Salvar", command=self.salvar)
        self.arquivo.add_command(label="Salvar como", command=self.salvar_como)
        self.arquivo.add_separator()
        self.arquivo.add_command(label="Voltar",command=self.voltar_pagina_inicial)
        self.barraMenu.add_cascade(label="Arquivo", menu=self.arquivo)  # Adicionando menu 'Arquivo' à barra de menu

        # Criação do menu 'Editar' com seus itens
        self.editar = Menu(self.barraMenu, tearoff=0)
        self.editar.add_command(label="Cortar", command=self.cortar)
        self.editar.add_command(label="Copiar", command=self.copiar)
        self.editar.add_command(label="Colar", command=self.colar)
        self.editar.add_command(label="Deletar", command=self.deletar)
        self.barraMenu.add_cascade(label="Editar", menu=self.editar)  # Adicionando menu 'Editar' à barra de menu

        # Área de texto
        self.texto = ScrolledText(self.root, width=1000, height=1000,font="arial 14")
        self.texto.place(x=5, y=0)
        self.texto.focus_force()

    def novo(self):
        """Limpa o texto no editor"""
        self.texto.delete('1.0', 'end')

    def abrir(self):
        """Abre um arquivo de texto"""
        self.root.filename = filedialog.askopenfilename(
            initialdir='/',
            title='Selecionar arquivo',
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if self.root.filename:
            with open(self.root.filename, 'r') as arquivo:
                conteudo = arquivo.read()
                self.texto.delete('1.0', 'end')
                self.texto.insert('end', conteudo)

    def salvar(self):
        """Salva o arquivo atual"""
        if not hasattr(self, 'root') or not self.root.filename:
            self.salvar_como()
        else:
            with open(self.root.filename, 'w') as arquivo:
                arquivo.write(self.texto.get('1.0', 'end'))

    def salvar_como(self):
        """Salva o arquivo em novo local"""
        self.root.filename = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if self.root.filename:
            with open(self.root.filename, 'w') as arquivo:
                arquivo.write(self.texto.get('1.0', 'end'))

    def cortar(self):
        """Corta o texto selecionado"""
        self.texto.event_generate("<<Cut>>")

    def copiar(self):
        """Copia o texto selecionado"""
        self.texto.event_generate("<<Copy>>")

    def colar(self):
        """Cola o texto copiado"""
        self.texto.event_generate("<<Paste>>")

    def deletar(self):
        """Deleta o conteúdo do texto"""
        deletar_tudo_mensagem = messagebox.askyesno("NeoNote", "Você deseja deletar tudo?")
        if deletar_tudo_mensagem:
            self.texto.delete('1.0', 'end')

    def voltar_pagina_inicial(self):
        from menu_principal import MenuPrincipal as m
        self.frame_caderno.destroy()
        self.texto.destroy()
        self.barraMenu.destroy()
        self.menuprincipal = m(self.root) 
        