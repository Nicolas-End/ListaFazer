from flask import Flask, request,render_template,flash
from datetime import datetime

from controllers.task_contrroler import tarefa
from config.config import DataBase

#criando um obejto que salva todos os dados dentra da tabel banco local
save = DataBase()  
save.create_new_database()

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('index.html')

#entrando na pagina para adicionar os itens ------------------------------------------------------------------
@app.route('/add-task')
def addPage():
    return render_template('add-task.html')

@app.route('/see-task')
def seePage():
    return render_template('see-task.html', array=save.get_tasks_to_do())

#serve para receber os dados do form add-task e colocar na lista e volta para a pagina index.html---------------
@app.route('/itens-add', methods=["POST"])
def add():

    task_name = request.form['name']
    task_description = request.form['desc']
    now = datetime.now().strftime('%H:%M')

    task = tarefa(task_name,task_description,now)

    save.add_new_task(task)
        
    return render_template('index.html')

@app.route('/del',methods=["POST"])
def dele():
    if request.method == "POST":
        button = [request.form['Valuebutton']]
        save.delDado(button)
    return render_template('index.html')
if __name__ == '__main__': 
    app.run()