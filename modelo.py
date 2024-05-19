import sqlite3

class AppBD():
    def __init__(self):
        self.create_table()
    
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('cadastro.db') 
        except sqlite3.Error as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
    
    def create_table(self):
        self.abrirConexao()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nascimento DATE NOT NULL,
            cpf INTEGER NOT NULL,
            senha VARCHAR NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Falha ao criar tabela", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.")
    def inserirDados(self, name, nascimento, cpf, senha):
        self.abrirConexao()
        insert_query = "INSERT INTO dados (name, nascimento, cpf, senha) VALUES (?, ?, ?, ?)"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (name, nascimento, cpf, senha))
            self.connection.commit()
            print("Produto inserido com sucesso")
        except sqlite3.Error as error:
            print("Falha ao inserir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.")
    def select_all_dados(self):
        self.abrirConexao()
        select_query = "SELECT * FROM dados"
        dados = [] 
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            dados = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar produtos", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.")
        return dados
    def update_dados(self, id, name, nascimento, cpf, senha):
        self.abrirConexao()
        update_query = "UPDATE dados SET name = ?, nascimento = ?, cpf = ?, senha = ? WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query, (name, nascimento, cpf, senha, id))
            self.connection.commit()
            print("Produto atualizado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao atualizar o produto", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.") 
    def delete_dados(self, id):
        self.abrirConexao()
        delete_query = "DELETE FROM dados WHERE id = ?"
        try:    
            cursor = self.connection.cursor()
            cursor.execute(delete_query, (id,)) 
            self.connection.commit()
            print("Produto deletado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao deletar produto", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada.")