const myButton = document.querySelector('button');

myButton.addEventListener('click', async () => {
    const tokenResponse = await fetch('http://localhost:9000/get-token',{
    mode: 'cors',
    method: 'POST',
    credentials: 'include',
})
    const data = await tokenResponse.json();
    const my_token = data.token;

    const tokenRevoke = await fetch('http://localhost:9000/revoke', {
        mode: 'cors',
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: my_token })
    });

    if (tokenRevoke.ok) {
        await fetch('http://localhost:9000/cleanup',{
        mode: 'cors',
        method: 'DELETE',
        credentials: 'include',
        })
    }
    window.location.href = 'http://localhost:4000/';
});