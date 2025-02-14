from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning,askyesno
from config import *
from tkcalendar import DateEntry
import locale
from tkinter import filedialog
from PIL import Image,ImageTk,ImageGrab
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
import os
from reportlab.platypus import Image

class Orcamento:
    def __init__(self,raiz,titulo):
        self.raiz = raiz 
        #self.raiz.protocol("WM_DELETE_WINDOW",self.mensagem_sair)

        #define o calendário para português
        locale.setlocale(locale.LC_TIME,"pt_BR.UTF-8")
        self.renderizar_div_lateral()
        self.renderizar_div_meio()

        self.total_acumulado = 0

    def mensagem_sair(self):
        if askyesno("Atenção","Tem certeza que deseja sair ?"):
            self.raiz.destroy()

    def renderizar_div_lateral(self):
        
        self.div_lateral = Frame(self.raiz,width=400,height=900)
        self.div_lateral.place(x=2,y=2)
        self.div_foto_empresa = LabelFrame(self.div_lateral,width=300,height=200)
        self.div_foto_empresa.place(x=100,y=5)

        self.label_cliente  = Label(self.div_lateral,text="CLIENTE",font="Arialblack 14 bold")
        self.label_cliente.place(x=150,y=210)

        self.label_foto = Label(self.div_foto_empresa)
        self.label_foto.pack(expand=True)

        self.botao_foto = Button(self.div_lateral,text="Escolher foto",command=self.escolher_foto,cursor="hand2")
        self.botao_foto.place(x=150,y=170)


        self.entrada_nome_cliente = Entry(self.div_lateral,font="Arialblack 14",fg="black")
        self.entrada_nome_cliente.place(x=20,y=240,width=350)
        self.entrada_nome_cliente.focus_force()
        self.placeholder_nome = "Informe quem é o cliente..."
        self.entrada_nome_cliente.insert(0,self.placeholder_nome)
        
        #placeholder nome
        self.entrada_nome_cliente.bind("<FocusIn>",self.remover_placeholder_nome)
        self.entrada_nome_cliente.bind("<FocusOut>",self.recolocar_placeholder_nome)

        self.label_data = Label(self.div_lateral,text="Data",font="Arialblack 14 bold")
        self.label_data.place(x=170,y=270)

        self.label_endereco = Label(self.div_lateral,text="ENDEREÇO",font="Arialblack 14 bold")
        self.label_endereco.place(x=140,y=340)

        self.label_cidade_estado_cep = Label(self.div_lateral,text="CIDADE e ESTADO OU CEP",font="Arialblack 14 bold")
        self.label_cidade_estado_cep.place(x=90,y=410)
        
        self.entrada_cidade_estado_cep = Entry(self.div_lateral,font="Arialblack 14")
        self.entrada_cidade_estado_cep.place(x=20,y=440,width=350)
        
        #placeholder cidade,estado ou cep

        self.entrada_cidade_estado_cep.bind("<FocusIn>",self.remover_placeholder_cidade_estado_cep)
        self.entrada_cidade_estado_cep.bind("<FocusOut>",self.recolocar_placeholder_cidade_estado_cep)

        self.placeholder_cidade_estado_cep = "Informe a cidade e estado ou CEP"
        self.entrada_cidade_estado_cep.insert(0,self.placeholder_cidade_estado_cep)

        self.entrada_data = DateEntry(self.div_lateral,font="Arialblack 14",width=12,date_pattern="dd/MM/yyyy",locale="pt_br",cursor="hand2")
        self.entrada_data.place(x=120,y=300)

        

        self.entrada_endereco_cliente = Entry(self.div_lateral,font="Arialblack 14",fg="black")
        self.entrada_endereco_cliente.place(x=20,y=370,width=350)


        #placeholder endereço 
        self.placeholder_endereco = "Informe o endereço do cliente..."
        self.entrada_endereco_cliente.insert(0,self.placeholder_endereco)
        self.entrada_endereco_cliente.bind("<FocusIn>",self.remover_placeholder_endereco)
        self.entrada_endereco_cliente.bind("<FocusOut>",self.recolocar_placeholder_endereco)


        #label telefone 
        self.label_telefone = Label(self.div_lateral,text="TELEFONE",font="Arialblack 14 bold")
        self.label_telefone.place(x=150,y=480)


        #entrada telefone 
        self.entrada_telefone = Entry(self.div_lateral,font="Arialblack 14",fg="black")
        self.entrada_telefone.place(x=20,y=510,width=350)

        #placeholder do telefone 

        self.placeholder_telefone = "Telefone para contato"
        self.entrada_telefone.insert(0,self.placeholder_telefone)
        self.entrada_telefone.bind("<FocusIn>",self.remover_placeholder_telefone)
        self.entrada_telefone.bind("<FocusOut>",self.recolocar_placeholder_telefone)


        #label email

        self.label_email = Label(self.div_lateral,text="E-MAIL",font="Arialblack 14 bold")
        self.label_email.place(x=150,y=540)

        #Entrada do e-mail
        self.entrada_email = Entry(self.div_lateral,font="arialblack 14")
        self.entrada_email.place(x=20,y=570,width=350)

        #Placeholder do e-mail
        self.placeholder_email = "Informe o seu email"

        self.entrada_email.insert(0,self.placeholder_email)
        self.entrada_email.bind("<FocusIn>",self.remover_placeholder_email)
        self.entrada_email.bind("<FocusOut>",self.recolocar_placeholder_email)

        #label  vendedor

        self.vendedor = Label(self.div_lateral,text="Vendedor",font="arialblack 14 bold")
        self.vendedor.place(x=150,y=600)

        #entrada do entry vendedor
        self.vendedor_entrada = Entry(self.div_lateral,font="arialblack 14")
        self.vendedor_entrada.place(x=20,y=630,width=350)

        #placeholder vendedor 

        self.placeholder_vendedor = "Nome do vendedor"

        self.vendedor_entrada.insert(0,self.placeholder_vendedor)
        self.vendedor_entrada.bind("<FocusIn>",self.remover_placeholder_vendedor)
        self.vendedor_entrada.bind("<FocusOut>",self.recolocar_placeholder_vendedor)

        self.atencao = Label(self.div_lateral,text="Este Orçamento é válido por 15 dias",font="Arialblack 14 bold",fg="red")
        self.atencao.place(x=5,y=670)

    def renderizar_icones(self, imagem_pasta, arquivo_nome):
        caminho_arquivo_icone = os.path.join(imagem_pasta, arquivo_nome)

        if not os.path.exists(caminho_arquivo_icone):
            showerror("Atenção", f"O arquivo {caminho_arquivo_icone} não foi encontrado!")
            return None
        return PhotoImage(file=caminho_arquivo_icone)


    def renderizar_div_meio(self):
        self.div_meio = Frame(self.raiz,width=996,height=800,bd=1)
        self.div_meio.place(x=400,y=2)

        frame_inputs = Frame(self.div_meio)
        frame_inputs.pack(pady=50)

        self.titulo_orcamento = Label(self.div_meio,text="PROPOSTA ORÇAMENTO DE SERVIÇOS",font="Arialblack 14 bold")
        self.titulo_orcamento.place(x=80,y=5)

        self.dados_empresa = Label(self.div_meio,text="Email: carlos.ronaldo.moura@gmail.com",font="Arialblack 12")
        self.dados_empresa.place(x=80,y=30)
        self.contato = Label(self.div_meio,text="Celular: (42) 92000-4376",font="Arialblack 12")
        self.contato.place(x=400,y=30)

        Label(self.div_meio,text="Lista de Materiais",font="Arialblack 14 bold").place(x=200,y=100)

        # Campos de entrada para os itens
        frame_inputs = Frame(self.div_meio)
        frame_inputs.pack(pady=50)

        Label(frame_inputs, text="QTD:", font="Arial 10 bold").grid(row=0, column=0, padx=5)
        self.entrada_qtd = Entry(frame_inputs, width=5)
        self.entrada_qtd.grid(row=0, column=1, padx=5)

        
        Label(frame_inputs, text="Material:", font="Arial 10 bold").grid(row=0, column=4, padx=5)
        self.entrada_descricao = Entry(frame_inputs, width=20)
        self.entrada_descricao.grid(row=0, column=5, padx=5)

        Label(frame_inputs, text="Preço Unitário (R$):", font="Arial 10 bold").grid(row=0, column=6, padx=5)
        self.entrada_preco = Entry(frame_inputs, width=10)
        self.entrada_preco.grid(row=0, column=7, padx=5)

        self.label_total = Label(self.div_meio, text="Total: R$ 0,00", font="Arial 14 bold")
        self.label_total.pack(pady=10, side="bottom")


        self.botao_adicionar = Button(frame_inputs, text="Adicionar Item", command=self.adicionar_item, cursor="hand2")
        self.botao_adicionar.grid(row=0, column=8, padx=10)

        self.icone_pdf = self.renderizar_icones("icones","upload.png")

        

        self.botao_voltar = Button(self.div_lateral,text="Voltar",bg="lightgreen",command=self.voltar,cursor="hand2")
        self.botao_voltar.place(x=80,y=700,width=150)

        self.div_observacoes = LabelFrame(self.raiz,width=300,height=440)
        self.div_observacoes.place(x=1050,y=230)

        Label(self.div_observacoes,text="Observação",font="arialblack 12 bold").place(x=100,y=4)

        self.texto_observacoes = Text(self.div_observacoes,font="arial 14")
        self.texto_observacoes.place(x=5,y=50,width=280,height=320)

        self.botao_gerar_pdf = Button(self.div_observacoes,text="Gerar PDF",image=self.icone_pdf,command=self.gerar_pdf,cursor="hand2")
        self.botao_gerar_pdf.place(x=120,y=397)

    
    def voltar(self):
        from menu_principal import MenuPrincipal 
        self.menu_principal = MenuPrincipal(self.raiz)
        self.div_lateral.destroy()
        self.div_meio.destroy()


    def atualizar_total(self):
        self.label_total.config(text=f"Total: R$ {self.total_acumulado:.2f}")

    def criar_tabela(self):
        self.colunas = ("QTD","Material","Preço Unitário","Total")

        self.tabela = ttk.Treeview(self.div_meio,columns=self.colunas,show="headings",height=20)

        for coluna in self.colunas:
            self.tabela.heading(coluna,text=coluna)
            self.tabela.column(coluna,width=120)
        
        self.tabela.pack(pady=10,fill="both",expand=True)

        self.botao_remover_item = Button(self.div_meio, text="Remover Item",command=self.remover_item,cursor="hand2")
        self.botao_remover_item.pack(pady=5)

    def adicionar_item(self):
        if not hasattr(self, 'tabela'):
            self.criar_tabela()
        self.qtd = self.entrada_qtd.get()
        
        self.descricao = self.entrada_descricao.get()
        self.preco_unitario = self.entrada_preco.get()

        if not self.qtd or not self.descricao or not self.preco_unitario:
            showerror("ERROR","PREENCHA TODOS OS CAMPOS!")
            return 

        try:
            self.qtd = int(self.qtd)
            self.preco_unitario = int(self.preco_unitario)
            self.total = self.qtd * self.preco_unitario
        
        except ValueError:
            showerror("ERROR","QUANTIDADE E PREÇO DEVEM SER NÚMEROS VÁLIDOS !")
            return 
        
        self.total_acumulado += self.total

        self.tabela.insert("","end",values=(self.qtd,self.descricao,f"R$ {self.preco_unitario:.2f}",f"R$ {self.total:.2f}"))
        
        self.entrada_qtd.delete(0,END)
        
        self.entrada_descricao.delete(0,END)
        self.entrada_preco.delete(0,END)

        self.atualizar_total()


    def remover_item(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            showwarning("AVISO","SELECIONE UM ITEM PARA REMOVER !")
            return

        for item in selecionado:
            total_item = self.tabela.item(item,"values")[3]
            total_item = float(total_item.replace("R$ ", "").replace(",", "."))
            self.total_acumulado -= total_item

            self.tabela.delete(item)

        self.atualizar_total()

    def escolher_foto(self):
        caminho_foto = filedialog.askopenfilename(title="Escolher uma imagem", filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

        if caminho_foto:
            self.imagem = Image.open(caminho_foto)
            self.imagem = self.imagem.resize((150, 150))  # Resize the image
            self.foto_tk = ImageTk.PhotoImage(self.imagem)  # Save the image
            self.label_foto.config(image=self.foto_tk)  # Update the label
    def remover_placeholder_vendedor(self,event):

        if self.vendedor_entrada.get() == self.placeholder_vendedor:
            self.vendedor_entrada.delete(0,END)
            self.vendedor_entrada.config(fg="gray")

    def recolocar_placeholder_vendedor(self,event):

        if self.vendedor_entrada.get() == "":
            self.vendedor_entrada.insert(0,self.placeholder_vendedor)
            self.vendedor_entrada.config(fg="black")


    def recolocar_placeholder_email(self,event):

        if self.entrada_email.get() == "":
            self.entrada_email.insert(0,self.placeholder_email)
            self.entrada_email.config(fg="black")

    def remover_placeholder_email(self,event):

        if self.entrada_email.get() == self.placeholder_email:
            self.entrada_email.delete(0,END)
            self.entrada_email.config(fg="gray")

    def remover_placeholder_endereco(self,event):

        if self.entrada_endereco_cliente.get() == self.placeholder_endereco:
            self.entrada_endereco_cliente.delete(0,END)
            self.entrada_endereco_cliente.config(fg="gray")
    
    def remover_placeholder_telefone(self,event):

        if self.entrada_telefone.get() == self.placeholder_telefone:
            self.entrada_telefone.delete(0,END)
            self.entrada_telefone.config(fg="gray")
    

    def recolocar_placeholder_telefone(self,event):

        if self.entrada_telefone.get() == "":
            self.entrada_telefone.insert(0,self.placeholder_telefone)
            self.entrada_telefone.config(fg="black")

    def recolocar_placeholder_endereco(self,event):

        if self.entrada_endereco_cliente.get() == "":
            self.entrada_endereco_cliente.insert(0,self.placeholder_endereco)
            self.entrada_endereco_cliente.config(fg="black")

    def remover_placeholder_nome(self,event):
        
        if self.entrada_nome_cliente.get() == self.placeholder_nome:
            self.entrada_nome_cliente.delete(0,END)
            self.entrada_nome_cliente.config(fg="gray")

    def recolocar_placeholder_nome(self, event):
        if self.entrada_nome_cliente.get() == "":
            self.entrada_nome_cliente.insert(0, self.placeholder_nome)
            self.entrada_nome_cliente.config(fg="black")

    def remover_placeholder_cidade_estado_cep(self,event):
        
        if self.entrada_cidade_estado_cep.get() == self.placeholder_cidade_estado_cep:
            self.entrada_cidade_estado_cep.delete(0,END)
            self.entrada_cidade_estado_cep.config(fg="gray")

    def recolocar_placeholder_cidade_estado_cep(self, event):
        if self.entrada_cidade_estado_cep.get() == "":
            self.entrada_cidade_estado_cep.insert(0, self.placeholder_cidade_estado_cep)
            
            self.entrada_cidade_estado_cep.config(fg="black")

    


    def gerar_pdf(self):
        # Verificar se há itens na tabela
        if not hasattr(self, 'tabela') or not self.tabela.get_children():
            showerror("Erro", "Nenhum item adicionado ao orçamento!")
            return

        # Permitir que o usuário selecione a imagem para o cabeçalho
        caminho_imagem = filedialog.askopenfilename(title="Escolha a imagem para o cabeçalho", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        
        if not caminho_imagem:
            showerror("Erro", "Nenhuma imagem escolhida.")
            return

        # Perguntar ao usuário o local para salvar o PDF
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not nome_arquivo:
            return

        # Criar o PDF
        pdf = SimpleDocTemplate(nome_arquivo, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Adicionar a imagem ao cabeçalho
        try:
            # Verificar se o arquivo da imagem existe
            if not os.path.exists(caminho_imagem):
                raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")

            # Adicionar a imagem ao cabeçalho (posição, largura, altura)
            img = Image(caminho_imagem, width=100, height=100)  # Ajuste o tamanho conforme necessário
            img.hAlign = 'LEFT'  # Alinhamento à esquerda (você pode mudar para 'CENTER' ou 'RIGHT')

            # Adicionar a imagem ao conteúdo do PDF
            story.append(img)
            story.append(Spacer(1, 12))

        except Exception as e:
            print(f"Erro ao adicionar imagem: {e}")
            showerror("Erro", f"Não foi possível adicionar a imagem ao cabeçalho: {e}")

        # Adicionar título e informações adicionais
        title = Paragraph("PROPOSTA ORÇAMENTO DE SERVIÇOS", styles['Title'])
        title2 = Paragraph("CRXR", styles['Title'])
        title3 = Paragraph("Email: carlos.ronaldo.moura@gmail.com", styles['Title'])
        title4 = Paragraph("Celular: 42 92000-4376", styles['Title'])

        story.append(title)
        story.append(Spacer(1, 12))
        story.append(title2)
        story.append(Spacer(1, 5))
        story.append(title3)
        story.append(Spacer(1, 5))
        story.append(title4)
        story.append(Spacer(1, 12))

        # Adicionar informações do cliente
        client_info = [
            f"Cliente: {self.entrada_nome_cliente.get()}",
            f"Endereço: {self.entrada_endereco_cliente.get()}",
            f"Cidade/Estado/CEP: {self.entrada_cidade_estado_cep.get()}",
            f"Telefone: {self.entrada_telefone.get()}",
            f"Email: {self.entrada_email.get()}",
            f"Vendedor: {self.vendedor_entrada.get()}",
            f"Data: {self.entrada_data.get()}"
        ]
        for info in client_info:
            story.append(Paragraph(info, styles['BodyText']))
            story.append(Spacer(1, 5))

        # Adicionar a seção "Lista de Materiais"
        lista_materiais_title = Paragraph("Lista de Materiais", styles['Heading2'])
        story.append(lista_materiais_title)
        story.append(Spacer(1, 12))

        # Adicionar o cabeçalho da tabela
        table_data = [["QTD", "Material", "Preço Unitário", "Total"]]

        # Adicionar os itens da tabela
        total_geral = 0
        for item in self.tabela.get_children():
            values = self.tabela.item(item, "values")
            qtd = values[0]
            descricao = values[1]
            preco_unitario = values[2].replace("R$ ", "")
            total_item = values[3].replace("R$ ", "")
            
            table_data.append([qtd, descricao, preco_unitario, total_item])
            total_geral += float(total_item.replace(",", "."))

        # Criar a tabela
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(table)
        story.append(Spacer(1, 12))

        # Adicionar o total
        total_geral_text = Paragraph(f"Total Geral: R$ {total_geral:.2f}", styles['BodyText'])
        story.append(total_geral_text)
        story.append(Spacer(1, 12))

        # Adicionar observações, se houver
        if self.texto_observacoes.get("1.0", "end-1c"):
            observacoes = Paragraph(f"Observações: {self.texto_observacoes.get('1.0', 'end-1c')}", styles['BodyText'])
            story.append(observacoes)

        # Construir o PDF
        pdf.build(story)
        showinfo("Sucesso", f"PDF gerado com sucesso em {nome_arquivo}")