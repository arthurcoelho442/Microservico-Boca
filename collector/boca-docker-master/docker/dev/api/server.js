// Importar o módulo HTTP
const http = require('http');

// Configurar o servidor HTTP para responder com "Olá, Mundo!" para todas as solicitações
const servidor = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Ola, Mundo!\n');
});

// Ouvir na porta 3000 e no endereço IP 127.0.0.1
const PORTA = 8080;
const IP = '0.0.0.0';

servidor.listen(PORTA, IP, () => {
  console.log(`Servidor rodando em http://${IP}:${PORTA}/`);
});