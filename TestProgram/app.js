const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const PORT = 4000;

const app = express();
app.use(cookieParser());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public'), {
  extensions: ['html']
}));




async function isLoggedIn(req, res, next) {
  const access_token = req.cookies.access_token;

  const response = await fetch('http://localhost:9000/validate-token',
  {
      mode: 'cors',
      method: 'POST',
      headers: {
      "Content-Type": "application/json",
      },
      credentials: 'include',
      body: JSON.stringify({token: access_token})
  })
  if (response.status === 200) {
    return next();
  } else {
  res.clearCookie('access_token', {
  httpOnly: true,
  });
  return res.redirect('http://localhost:4000/');
  }};


app.use('/private', isLoggedIn, express.static(path.join(__dirname, 'private'), {
  extensions: ['html']
}));

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});