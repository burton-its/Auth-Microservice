const express = require('express');
const path = require('path');
const PORT = 4000;

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));


app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});