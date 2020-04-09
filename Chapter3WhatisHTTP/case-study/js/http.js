/*
	Author: John Royce C. Punay
	Date created: April 9, 2020 5:00PM
*/

'use strict'
const http = require("http")

const server = http.createServer((request, response) => {
    response.on('end', () => {
        console.log('client disconnected');
    });
    response.setHeader('Set-Cookie', ['type=ninja', 'language=js']);
    response.setHeader('Content-type', 'text/html');
    response.writeHead(200)
    response.write(
        `<p style="font-size: 13px;">Hello worlsd</p>
            <script>
                var a = 1;
                alert(1)
            </script>
        `
    );
    response.end();
});
server.listen(5000, "127.0.0.1", () => {
    console.log('Server is up waiting for connections');
});

server.on("close", () => {
    console.log('Server is close bye!');
});

// RESOURCES 
//https://nodejs.org/dist/latest-v12.x/docs/api/net.html#net_server_close_callback (Node: v12.x)
// Open browser then put on the link: http://127.0.0.1:5000/
// https://www.w3schools.com/nodejs/nodejs_http.asp
// https://flaviocopes.com/http-curl/#perform-an-http-get-request Use CURL on CLI