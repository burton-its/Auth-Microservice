// Remove access token on refresh or navigation
window.addEventListener('beforeunload', () => {
    if (localStorage.getItem('token')) {
        localStorage.removeItem('token');
    }
});