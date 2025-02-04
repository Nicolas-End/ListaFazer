function tasks(){
    fetch ('http://127.0.0.1:5000/see-task',{
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    })

    .then(response => response.json()
    )

    .then(data=> {
        console.log(data)
    }  )
    .catch(error =>{
        console.log('Error: ',error)
        throw error
    }
    )

}


const div = document.getElementById('product-div')
const ul = document.createElement('ul')


