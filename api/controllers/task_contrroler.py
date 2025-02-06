from config.config import DataBase
from datetime import datetime , timedelta
from config.config import DataBase


class TaskController:

    def __init__(self):
        self.database = DataBase()
        self.coll = self.database.coll

    def add_new_task_to_database(self,name,desc):
        
        try: 

            
            name_exist_filter = {
                "task_name":name
            }
            if self.coll.find_one(name_exist_filter):
                return False,"Task already exist"
            
            self.time_now = str(datetime.now())
            self.coll.create_index([('expireAt',1)], expireAfterSeconds=1800)

            task_data = {
                "task_name":name,
                "task_description":desc,
                "task_hour_made":self.time_now,
                "expireAt": datetime.utcnow() + timedelta(seconds=1800)
            }
            self.coll.insert_one(task_data)

            return True,"Ok"
        
        except Exception as e:
            print('Error: ',e)
            return False,"Excpetion Error"
        
    def return_tasks_in_database(self,cursor):
        try:
            
            tasks_in_database = []
            self.id_to_item = 0

            for document in cursor:

                self.id_to_item = self.id_to_item+1
                document.pop('_id')
                document['id'] = self.id_to_item

                tasks_in_database.append(document)
                
            return  tasks_in_database
        
        except Exception as e:
            print('Error: ',e )
            return False
    
    def get_tasks_to_do(self):
        try:

            cursor = self.coll.find({})

            tasks_in_database = self.return_tasks_in_database(cursor=cursor)

            return tasks_in_database

        except Exception as e:
            print('Error: ',e)
            return False,'Excpetion Error'

    def delete_task_by_name(self,name):
        try:
            self.name_finder = {'task_name':name}

            if not self.coll.find_one(self.name_finder):
                return False
            
            self.coll.find_one_and_delete(self.name_finder)
            return True
        except Exception as e:
            print('Error: ',e)
            return False