from flask import Flask, request,render_template,flash
from datetime import datetime
#importandos as instacias criadas por mim para fazer as funcionalidades dos projeto
from produtos import tarefa , banco
#criando um obejeto que salva todos os dados dentra da tabel banco local
save = banco()  
save.daTarefas()
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
    return render_template('see-task.html', array=save.get_dados())
#serve para receber os dados do form add-task e colocar na lista e volta para a pagina index.html---------------
@app.route('/itens-add', methods=["POST"])
def add():
    #se o method é post ele pega os dados
    if request.method == 'POST':
        #pegando o nome e a descrição da tarefa
        nome = request.form['name']
        desc = request.form['desc']
        now = datetime.now().strftime('%H:%M')
        #criando um objeto com esse dados
        task = tarefa(nome,desc,now)
        #adicionando os dados ao banco
        save.addDados(task)
    return render_template('index.html')
@app.route('/del',methods=["POST"])
def dele():
    if request.method == "POST":
        button = [request.form['Valuebutton']]
        save.delDado(button)
    return render_template('index.html')
if __name__ == '__main__': 
    app.run()