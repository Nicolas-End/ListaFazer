from flask import Flask, request,render_template,flash,jsonify
from flask_cors import CORS
from datetime import datetime

from controllers.task_contrroler import TaskController
from config.config import DataBase


#criando um obejto que salva todos os dados dentra da tabel banco local
save = DataBase()  
save.create_new_database()

app = Flask(__name__)
CORS(app, origins="*")


@app.route('/see-task', methods=["GET"])
def seePage():
    try:
        list_task = DataBase().get_tasks_to_do()

        return jsonify(list_task),201
    
    except Exception as e:

        print('Error: ',e)
        return jsonify('Error'),500


@app.route('/itens-add', methods=["POST"])
def add():
    try:
        
        response = request.get_json()
        
        if TaskController(response['name'],response['desc']).add_new_task_to_database():
            return jsonify({'status':'ok'}), 201
            
        else:
            return  jsonify({'status':'error'}), 500


        

    except Exception as e:
        print("Error: ",e)
        return jsonify({'status':'error'}), 500

@app.route('/del',methods=["POST"])
def dele():
    try:
        response = request.get_json()

        if save.delete_task_from_database(response['id']):
            return jsonify({'status':'ok'}),201
        
        return jsonify({'status':'error'}),500
    
    except Exception as e:
        print('Error: ',e)   
        return jsonify({'status':'error'}),500
    
if __name__ == '__main__': 
    app.run()