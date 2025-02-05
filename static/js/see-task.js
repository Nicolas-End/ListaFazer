function fetch_tasks(ul){

    fetch ('http://127.0.0.1:5000/see-task',{
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    })

    .then(response => response.json()
    )

    .then(data=> {
        ul.innerHTML = ''
        data.forEach(element => {
            console.log(element)
            const li = document.createElement('li')
            li.appendChild(createSpan(element))
            li.appendChild(createDiv(element))
            li.appendChild(createDeleteForm(element))
            ul.appendChild(li)
        });
        ActionListenerForm()
    }  )
    .catch(error =>{
        console.log('Error: ',error)
        throw error
    }
    )

}

function createSpan(element){

    const span = document.createElement('span')
    span.className = 'task-number'
    span.textContent = (element['id'])
    return span

}

function createDiv(element){

    const div = document.createElement('div')
    const pName = document.createElement('p')
    const pDesc = document.createElement('p')
    const pHours = document.createElement('p')

    pName.textContent = `Nome da Tarefa: ${element['task_name']}`
    pDesc.textContent = `Descrição da Tarefa: ${element['task_description']}`
    pHours.textContent = `Horario de Inicialização da Tarefa: ${element['task_hour_made']}`

    div.appendChild(pName)
    div.appendChild(pDesc)
    div.appendChild(pHours)
    return div
}

function createDeleteForm(element){

    const form = document.createElement('form')
    const button = document.createElement('button')

    button.value = element['task_name']

    button.textContent = "Eliminar Tarefa"
    button.type = 'submit'
    button.className = 'deleteButton'

    form.className="formDelete"
    
    form.appendChild(button)

    return form
}

function ActionListenerForm(){
    const forms = document.getElementsByClassName('formDelete');

    for (let i = 0; i < forms.length; i++) {
        forms[i].addEventListener('submit', function(event) {
            event.preventDefault(); 

            const button = event.target.querySelector('.deleteButton'); 

            fetch('http://127.0.0.1:5000/del', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task_name: button.value }) 
            })
            .then(response => response.json())
            .then(data => {
                if (data.status == "ok"){
                    location.reload()
                    alert('Tarefa Eliminada!!!')
                    return 
                }
                alert('Opps!!, houve algum erro')
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
}
}

function Initial(){

    const div = document.getElementById('product-div')
    const ul = document.createElement('ul')
    div.appendChild(ul)

    fetch_tasks(ul)

}
Initial()