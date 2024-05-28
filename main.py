import tkinter as tk
from tkinter import ttk
import modelo as crud

class PrincipalBD():
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.janela = win
        self.treeDados = ttk.Treeview(self.janela, 
                                              columns=("Id da Missão",
                                                        "Nome da Missão", 
                                                        "Data de Lançamento",
                                                        "Destino",
                                                        "Estado da Missão",
                                                        "Tripulação",
                                                        "Carga",
                                                        "Duração da Missão",
                                                        "Custo da Missão",
                                                        "Status da Missão"),
                                              show="headings") 
        self.treeDados.heading("Id da Missão", text="Id da Missão:")
        self.treeDados.heading("Nome da Missão", text="Nome da Missão:")
        self.treeDados.heading("Data de Lançamento", text="Data de Lançamento:")
        self.treeDados.heading("Destino", text="Destino:")
        self.treeDados.heading("Estado da Missão", text="Estado da Missão:")
        self.treeDados.heading("Tripulação", text="Tripulação:")
        self.treeDados.heading("Carga", text="Carga:")
        self.treeDados.heading("Duração da Missão", text="Duração da Missão:")
        self.treeDados.heading("Custo da Missão", text="Custo da Missão:")
        self.treeDados.heading("Status da Missão", text="Status da Missão:")
        self.treeDados.pack()

        self.fExibirTela()

        self.lblNome = tk.Label(self.janela, text="Nome da Missão:", font="Arial", background="#87CEEB")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblData = tk.Label(self.janela, text="Data de Lançamento:",font="Arial", background="#87CEEB")
        self.lblData.pack()
        self.entryData = tk.Entry(self.janela)
        self.entryData.pack()

        self.lblDestino = tk.Label(self.janela, text="Destino:", font="Arial", background="#87CEEB")
        self.lblDestino.pack()
        self.entryDestino = tk.Entry(self.janela)
        self.entryDestino.pack()

        self.lblEstado = tk.Label(self.janela, text="Estado da Missão:", font="Arial", background="#87CEEB")
        self.lblEstado.pack()
        self.entryEstado = tk.Entry(self.janela)
        self.entryEstado.pack()

        self.lblTripulacao = tk.Label(self.janela, text="Tripulação:", font="Arial", background="#87CEEB")
        self.lblTripulacao.pack()
        self.entryTripulacao = tk.Entry(self.janela)
        self.entryTripulacao.pack()

        self.lblCarga = tk.Label(self.janela, text="Carga:", font="Arial", background="#87CEEB")
        self.lblCarga.pack()
        self.entryCarga = tk.Entry(self.janela)
        self.entryCarga.pack()

        self.lblDuração = tk.Label(self.janela, text="Duração da Missão:", font="Arial", background="#87CEEB")
        self.lblDuração.pack()
        self.entryDuração = tk.Entry(self.janela)
        self.entryDuração.pack()

        self.lblCusto = tk.Label(self.janela, text="Custo da Missão:", font="Arial", background="#87CEEB")
        self.lblCusto.pack()
        self.entryCusto = tk.Entry(self.janela)
        self.entryCusto.pack()

        self.lblStatus = tk.Label(self.janela, text="Status da Missão:", font="Arial", background="#87CEEB")
        self.lblStatus.pack()
        self.entryStatus = tk.Entry(self.janela)
        self.entryStatus.pack()
        
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
            data = self.entryData.get()
            destino = self.entryDestino.get()
            estado = self.entryEstado.get()
            tripulacao = self.entryTripulacao.get()
            carga = self.entryCarga.get()
            duracao = self.entryDuração.get()
            custo = self.entryCusto.get()
            status = self.entryStatus.get()
            self.objBD.inserirDados(name, data, destino, estado, tripulacao, carga, duracao, custo, status)
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryData.delete(0, tk.END)
            self.entryDestino.delete(0, tk.END)
            self.entryEstado.delete(0, tk.END)
            self.entryTripulacao.delete(0, tk.END)
            self.entryCarga.delete(0, tk.END)
            self.entryDuração.delete(0, tk.END)
            self.entryCusto.delete(0, tk.END)
            self.entryStatus.delete(0, tk.END)
            print('Informações Cadastradas com Sucesso!')
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
            data = self.entryData.get()
            destino = self.entryDestino.get()
            estado = self.entryEstado.get()
            tripulacao = self.entryTripulacao.get()
            carga = self.entryCarga.get()
            duracao = self.entryDuração.get()
            custo = self.entryCusto.get()
            status = self.entryStatus.get()
            self.objBD.update_dados(id, name, data, destino, estado, tripulacao, carga, duracao, custo, status) #método update_product() do objeto objBD para atualizar as informações do produto no banco de dados
            self.fExibirTela()

            self.entryNome.delete(0, tk.END)
            self.entryData.delete(0, tk.END)
            self.entryDestino.delete(0, tk.END)
            self.entryEstado.delete(0, tk.END)
            self.entryTripulacao.delete(0, tk.END)
            self.entryCarga.delete(0, tk.END)
            self.entryDuração.delete(0, tk.END)
            self.entryCusto.delete(0, tk.END)
            self.entryStatus.delete(0, tk.END)
            print('Informações Atualizadas com Sucesso!')        
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

            print('Informações Deletadas com Sucesso.')
        except:
            print('Não foi possivel deletar.')
    
janela = tk.Tk() 
product_app = PrincipalBD(janela) 
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("900x900")
janela.configure(background="#87CEEB")


janela.mainloop() 
