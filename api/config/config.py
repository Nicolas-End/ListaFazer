from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class DataBase:
    def __init__(self):
        try:
            self.uri_name = os.getenv('MONGO_URI')
            self.database_name = os.getenv('DATABASE_NAME')
            self.collection_name = os.getenv('COLLECTION_NAME')
            
            if not self.uri_name or not self.database_name or not self.collection_name:
                raise ValueError("O .env não esta configurado corretamente")

            self.client = MongoClient(self.uri_name,serverSelectionTimeoutMS=5000)
            self.database = self.client[self.database_name]
            self.coll = self.database[self.collection_name]

        except Exception as e:
            print('Error: ',e)
            return None
