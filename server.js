'use strict';

const express = require('express');
const app = express();

const PORT = 8080;
const HOST = '0.0.0.0';

// Application
app.get('/', (req, res) => {
    res.send("Hello world test5");
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`)
