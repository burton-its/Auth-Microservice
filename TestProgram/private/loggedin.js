const myButton = document.querySelector('button');

myButton.addEventListener('click', async () => {
    console.alert('CLICKED')
});

// Remove access token on refresh or navigation
window.addEventListener('beforeunload', () => {
    if (localStorage.getItem('token')) {
        localStorage.removeItem('token');
    }
});