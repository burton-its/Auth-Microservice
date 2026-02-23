const header = document.querySelector('h1')
const userEmail = document.getElementById('user_email');
const userPassword = document.getElementById('user_password');
const loginForm = document.getElementById('loginForm');

function browserAlert(message) {
    alert(message);
}

document.addEventListener('DOMContentLoaded', async (req, res) => {
       const response = 
            await fetch('http://localhost:8000/',{
            mode: 'cors',
        })

        const data = await response.json();
        header.textContent = data.message;
});

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
     const payload = {
        email: userEmail.value,
        password: userPassword.value
    };
    const response = await fetch('http://localhost:8000/auth/login',{
        mode: 'cors',
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    const data = await response.json();
    if (!data.access_token) {
        browserAlert(data.detail);
    } else {
        localStorage.setItem('token', data.access_token);
        browserAlert('Login verified with access token');
        window.location.replace('./loggedin.html');
    }
});
