from flask import Flask, request,render_template,flash,jsonify
from flask_cors import CORS
from datetime import datetime

from controllers.task_contrroler import TaskController

task = TaskController()



app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def home():
    return "<h1> Seja Bem Vindo a minha Api</h1>"

@app.route('/see-task', methods=["GET"])
def seePage():
    try:
        list_task = task.get_tasks_to_do()
        if list_task:
            return jsonify(list_task),201
        return jsonify('Error'),500
    
    except Exception as e:

        print('Error: ',e)
        return jsonify('Error'),500


@app.route('/itens-add', methods=["POST"])
def add():
    try:
        
        response = request.get_json()
        
        returnServer, responseTask = task.add_new_task_to_database(name=response['name'],desc=response['desc'])
            
        if returnServer:
            return jsonify({'status':'ok'}), 201
            
        else:
            return  jsonify({'status':responseTask}), 500


        

    except Exception as e:
        print("Error: ",e)
        return jsonify({'status':'error'}), 500

@app.route('/del',methods=["POST"])
def dele():
    try:
        response = request.get_json()
        
        if task.delete_task_by_name(response['task_name']):
            return jsonify({'status':'ok'}),201
        
        return jsonify({'status':'error'}),500
    
    except Exception as e:
        print('Error: ',e)   
        return jsonify({'status':'error'}),500
    
if __name__ == '__main__': 
    app.run()