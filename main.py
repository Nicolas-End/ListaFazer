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
    return jsonify({'Status':'Ok'})
    #return render_template('see-task.html', array=save.get_tasks_to_do())

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
    if request.method == "POST":
        button = [request.form['Valuebutton']]
        save.delDado(button)
    return render_template('index.html')
if __name__ == '__main__': 
    app.run()