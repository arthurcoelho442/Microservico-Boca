# Use a imagem base Node.js
FROM node:14

# Copia o diretório para dentro do container
COPY ./boca-docker/docker/dev/api/ ./app

# Define o diretório de trabalho no container
WORKDIR /app

# Instale as dependências do aplicativo
RUN npm install

# Exponha a porta em que o aplicativo será executado
EXPOSE 8080

# Comando para iniciar o aplicativo quando o contêiner for iniciado
CMD ["npm", "start"]