import mysql.connector
# Criando uma classe para salvar os dados do usuario----------------------------------------------------------
class tarefa:
    def __init__(self,nome,desc,horas):
        self.nome = nome
        self.desc = desc
        self.horas = horas
#criando uma outra classe para colocar os dados do usuario em um banco de dados local--------------------------
class banco:
    # fazendo ligação com o banco de dados---------------------------------------------------------------------
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nicolas123"
        )
        self.cursor = self.mydb.cursor()
    #criar a tabela tarefas caso n exista
    def daTarefas(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS tarefas")
        self.cursor.execute("USE tarefas")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lista(id int auto_increment not null, nome varchar(60) not null, descri text, timer varchar(20),primary key(id));")
    def addDados(self,dados):
        #adiciona dados a tabela tarefas.lista
        self.cursor.execute("USE tarefas")
        addsql = "INSERT INTO lista (nome,descri,timer) VALUES (%s,%s,%s)"
        values = (dados.nome,dados.desc,dados.horas)
        self.cursor.execute(addsql,values)
        self.mydb.commit()
    #pega os dados da tabela para ser mostrado na pagina see-task
    def get_dados(self):
        self.cursor.execute("USE tarefas")
        self.cursor.execute("SELECT * FROM lista")
        bancoLinha = self.cursor.fetchall()
        array = []
        for i in bancoLinha:
            array.append(i)
        return array
    #reorganiza e deleta o dados de acordo com o id escolhido pelo usuario
    def delDado(self,id):
        self.cursor.execute("USE tarefas")
        self.id = id
        dele = "DELETE FROM lista WHERE id = %s  "
        self.value = (self.id)
        self.cursor.execute(dele,self.value)
        #reorganizando os id do produto dando um "sort"
        self.cursor.execute("SET @count = 0;")
        self.cursor.execute("UPDATE lista SET id = @count:= @count + 1;")
        self.cursor.execute("ALTER TABLE lista AUTO_INCREMENT = 1;")
        self.mydb.commit()

        

