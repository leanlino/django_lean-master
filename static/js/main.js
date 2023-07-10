const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const formulario = document.getElementById('formulario')
console.log(formulario);

formulario.addEventListener('submit', (e) => {
    e.preventDefault()
    const form = Object.fromEntries(new FormData(e.target))
    console.log(form);
    try {
        fetch('/api/form', {
            method: 'POST',
            body: JSON.stringify(form),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        })
            .then(response => {
                if (response.ok) {
                    console.log('ok')
                    alert("Su formulario ha sido enviado")
                }
                
            })

            .catch(
                error => {
                    console.log(error);
                }
            );

    } catch (error) {

        console.log(error);
        
    }
    formulario.reset()
})
