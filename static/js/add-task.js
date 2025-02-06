document.getElementById('add_form').addEventListener('submit',
    function(event){
        event.preventDefault();

    const name = document.getElementById('inputName').value
    const description = document.getElementById('inputId').value

    fetch('https://lista-fazer-eta.vercel.app/itens-add',{
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: name ,desc:description})
    })
    .then(response => response.json())
    .then(data => 
    {
        if (data.status === 'ok'){
            document.getElementById('inputName').value = ''
            document.getElementById('inputId').value = ''
            alert('Nova Tarefa Adicionada com sucesso')
        }
        else if (data.status == 'Task already exist'){
            document.getElementById('inputName').value = ''
            document.getElementById('inputId').value = ''
            alert('Esta tarefa já existe')
        }
        else{
            document.getElementById('inputName').value = ''
            document.getElementById('inputId').value = ''
            alert('Opps!!, a tarefa não foi adicionada com exito')
        }
    }
    )
    }
)