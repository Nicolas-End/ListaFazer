import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
# Criando uma classe para salvar os dados do usuario----------------------------------------------------------

#criando uma outra classe para colocar os dados do usuario em um banco de dados local--------------------------
class DataBase:
    # fazendo ligação com o banco de dados---------------------------------------------------------------------
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        self.cursor = self.mydb.cursor()
   
    def create_new_database(self):

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS tarefas")
        self.cursor.execute("USE tarefas")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lista(id int auto_increment not null, nome varchar(60) not null, descri text, timer varchar(20),primary key(id));")
    
    def add_new_task(self,task):

        self.cursor.execute("USE tarefas")

        addsql = "INSERT INTO lista (nome,descri,timer) VALUES (%s,%s,%s)"
        values = (task.nome,task.desc,task.horas)
        self.cursor.execute(addsql,values)

        self.mydb.commit()
    
    def get_tasks_to_do(self):
        
        self.cursor.execute("USE tarefas")
        self.cursor.execute("SELECT * FROM lista")

        self.database_datas = self.cursor.fetchall()
        self.array_tasks = []

        for i in self.database_datas:
            self.array_tasks.append(i)
        return self.array_tasks
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

        

