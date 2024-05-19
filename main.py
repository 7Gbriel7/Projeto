import tkinter as tk
from tkinter import ttk
import modelo as crud

class PrincipalBD():
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.janela = win
        self.treeDados = ttk.Treeview(self.janela, 
                                              columns=("Código",
                                                        "Nome", 
                                                        "Data de Nascimento",
                                                        "CPF",
                                                        "Senha"),
                                              show="headings") 
        self.treeDados.heading("Código", text="Código:")
        self.treeDados.heading("Nome", text="Nome:")
        self.treeDados.heading("Data de Nascimento", text="Data de Nascimento:")
        self.treeDados.heading("CPF", text="CPF")
        self.treeDados.heading("Senha", text="Senha:")
        self.treeDados.pack()

        self.fExibirTela()

        self.lblNome = tk.Label(self.janela, text="Nome:", font="Arial", background="#87CEEB")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblData = tk.Label(self.janela, text="Data de Nascimento:",font="Arial", background="#87CEEB")
        self.lblData.pack()
        self.entryData = tk.Entry(self.janela)
        self.entryData.pack()

        self.lblCPF = tk.Label(self.janela, text="CPF:", font="Arial", background="#87CEEB")
        self.lblCPF.pack()
        self.entryCPF = tk.Entry(self.janela)
        self.entryCPF.pack()

        self.lblSenha = tk.Label(self.janela, text="Senha:", font="Arial", background="#87CEEB")
        self.lblSenha.pack()
        self.entrySenha = tk.Entry(self.janela)
        self.entrySenha.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Cadastrar", command=self.Cadastrar, background="white", font="Arial")
        self.btnCadastrar.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Atualizar", command=self.Atualizar, background="white", font="Arial")
        self.btnCadastrar.pack()

        self.btnCadastrar = tk.Button(self.janela, text = "Deletar", command = self.Deletar, background="white", font="Arial")
        self.btnCadastrar.pack()

    def fExibirTela(self):
        try:
            self.treeDados.delete(*self.treeDados.get_children())
            dados = self.objBD.select_all_dados() 
            for dados in dados:
                self.treeDados.insert("", tk.END, values=dados)
        except:
            print('Não foi possível exibir os campos.')
        
    def Cadastrar(self):
        try:
            name = self.entryNome.get()
            nascimento = self.entryData.get()
            cpf = self.entryCPF.get()
            senha = self.entrySenha.get()
            self.objBD.inserirDados(name, nascimento, cpf, senha)
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryData.delete(0, tk.END)
            self.entryCPF.delete(0, tk.END)
            self.entrySenha.delete(0, tk.END)
            print('dados Cadastrados com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')

    def Atualizar(self):
        try:
            selected_item = self.treeDados.selection() #A função selection() retorna uma lista contendo o identificador do item selecionado.
            if not selected_item:
                return
            item = self.treeDados.item(selected_item)
            dados = item['values']
            id = dados[0]
            name =  self.entryNome.get()
            nascimento = self.entryData.get()
            cpf = self.entryCPF.get()
            senha = self.entrySenha.get()
            self.objBD.update_dados(id, name, nascimento, cpf, senha) #método update_product() do objeto objBD para atualizar as informações do produto no banco de dados
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryData.delete(0, tk.END)
            self.entryCPF.delete(0, tk.END)
            self.entrySenha.delete(0, tk.END)
            print('Dados Atualizados com Sucesso!')        
        except:
            print('Não foi possível fazer a atualização.')

    def Deletar(self):
        try:
            selected_item = self.treeDados.selection()
            if not selected_item:
                return
            item = self.treeDados.item(selected_item)
            dados = item['values']
            id = dados[0]
            self.objBD.delete_dados(id)
            self.fExibirTela()

            print('Dados Deletados com Sucesso.')
        except:
            print('Não foi possivel deletar.')
janela = tk.Tk() 
product_app = PrincipalBD(janela) 
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("1000x700")
janela.configure(background="#87CEEB")


janela.mainloop() 
