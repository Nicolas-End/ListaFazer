import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class DataBase:
    
    def __init__(self):
        try:
            hostName = str(os.getenv('HOST'))
            userName = str(os.getenv('USER'))
            passwordAcess = str(os.getenv('PASSWORD')) 
            self.mydb = mysql.connector.connect(
                host= hostName,
                user= userName,
                password= passwordAcess
            )
            self.cursor = self.mydb.cursor()
        except Exception as e:
            print("Error: ",e )
   
    def create_new_database(self):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS tarefas")
            self.cursor.execute("USE tarefas")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS lista(id int auto_increment not null, nome varchar(60) not null, descri text, hour varchar(20),primary key(id));")
        except Exception as e:
            print("Error: ",e)

    def add_new_task(self,name,desc,hours):

        self.cursor.execute("USE tarefas")

        addsql = "INSERT INTO lista (nome,descri,hour) VALUES (%s,%s,%s)"
        values = (name,desc,hours)
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

    def delete_task_from_database(self,id):
        try:
            id = (int(id))

            self.cursor.execute("USE tarefas")

            self.id = id
            dele = "DELETE FROM lista WHERE id = %s  "
            self.value = [self.id]
            
            self.cursor.execute(dele,self.value)

            #reorganizando os id do produto dando um "sort"
            self.cursor.execute("SET @count = 0;")
            self.cursor.execute("UPDATE lista SET id = @count:= @count + 1;")
            self.cursor.execute("ALTER TABLE lista AUTO_INCREMENT = 1;")

            self.mydb.commit()
            return True
        
        except Exception as e:
            print('Error: ',e)
            return False

        

