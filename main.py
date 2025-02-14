import tkinter as tk
from caderno import *
from config import *
from menu_principal import *
from agenda import *
from orcamento import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NeoNote")
        self.root.resizable(0,0)
        self.root.geometry(f"{largura_janela}x{altura_janela}+200+50")

        #self.tela_menu = MenuPrincipal(self.root)
        #self.agenda_teste = Agenda(self.root,titulo_agenda)
        self.orcamento_frame  = Orcamento(self.root,titulo_orcamento)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.state('zoomed')
    root.mainloop()
