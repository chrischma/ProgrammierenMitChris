const http = require('http');
const port = 3000

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hallo Welt!');
});

server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
})
