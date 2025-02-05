document.getElementById('add_form').addEventListener('submit',
    function(event){
        event.preventDefault();

    const name = document.getElementById('inputName').value
    const description = document.getElementById('inputId').value

    fetch('http://127.0.0.1:5000/itens-add',{
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
        else{
            document.getElementById('inputName').value = ''
            document.getElementById('inputId').value = ''
            alert('A nova tarefa não foi adicionada')
        }
    }
    )
    }
)