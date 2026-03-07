const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const PORT = 4000;

const app = express();
app.use(cookieParser());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));


async function isLoggedIn(req, res) {
  const access_token = req.cookies.access_token;
  if (access_token) {
    const isValid = await fetch('http://localhost:9000/validate-token',
      {
          mode: 'cors',
          method: 'POST',
          credentials: 'include',
          body: JSON.stringify(access_token)
      });
  }
  res.redirect('/login'); // Redirect to login page if not authenticated
}


app.use('/private', isLoggedIn, express.static(path.join(__dirname, 'private')));

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});