# Estágio de construção
FROM python:3.10

# Rótulo personalizado para o nome da imagem
LABEL app_name="microserviceboca"
LABEL app_version="latest"

# Copia o diretório para dentro do container
COPY ./api ./app

# Define o diretório de trabalho no container
WORKDIR /app

# Instala a biblioteca com todas as suas dependências definidas no requirements.txt
RUN pip install -r ./requirements.txt

# Expondo a porta em que o aplicativo será executado
EXPOSE 8080

# Comando para iniciar o aplicativo quando o contêiner for iniciado
CMD python ./run.py