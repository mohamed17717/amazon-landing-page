var StaticServer = require('static-server');
var server = new StaticServer({
    rootPath: './dist/',
    port: 1337,
    
})

server.start(function(){
    console.log('Server lestening to ', 'http://127.0.0.1:'+server.port);
})

// you can run server by
// node <fileName>