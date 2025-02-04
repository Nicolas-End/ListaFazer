from config.config import DataBase
from datetime import datetime
class TaskController:

    def __init__(self,name,desc):
        self.name = name
        self.description = desc
        self.hours = datetime.now().strftime('%H:%M:%S')

    def add_new_task_to_database(self):
        
        try: 
            self.save = DataBase()  
            self.save.create_new_database()

            self.save.add_new_task(self.name,self.description,self.hours)
            return True
        
        except Exception as e:
            print('Error: ',e)
            return False

