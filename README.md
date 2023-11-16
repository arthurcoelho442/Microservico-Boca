# Microservico-Boca

<div  Align="justify">
<div Align="center"><img src="https://private-user-images.githubusercontent.com/56831082/283241586-9e9c6b6a-24d3-4b3c-b3c0-fc4bd1733ded.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNDE1ODYtOWU5YzZiNmEtMjRkMy00YjNjLWIzYzAtZmM0YmQxNzMzZGVkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVjYWVhYjViNWIyMGI2YWE4ZjE0MzNkMWZmYzEzYjFhMTJhZTBmYjc4OTZjN2I5NGI5NmEwMDQ0Nzc1ZjNhNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.B0NQ0g4ba0ZeKv-gsKttrxAIU85rJVcSEuwfzEhcVZ8" height = 400 width=900> </div>

# Sumario
- [Objetivo do Trabalho](#Objetivo-do-Trabalho)
- [Mode de Execucao](#Mode-de-Execucao)
  - [Configuração](#Configuração)
  - [Execução](#Execução)
  - [Visualização](#Visualizção)
- [Funcionamento](#Funcionamento)
  - [API](#API)
  - [Exemplos](#Exemplos)

# <a name=“Objetivo-do-Trabalho”><a/>Objetivo do Trabalho
Consiste no desenvolvimento de parte de um microsserviço de back-end que permite a aplicações clientes (por ex., front-end ou Application Programming Interface client) gerenciar turmas e objetos de aprendizagem armazenados em um SGBD através de uma API REST. Este trabalho oportuniza a prática dos conhecimentos obtidos na disciplina com tecnologias atuais e em um sistema real, o ambiente BOCA (BOCA Online Contest Administrator), o qual é usado para gerenciar competições da Maratona de Programação da SBC e do Topcom, e, mais recentemente, como ferramenta de apoio em disciplinas de programação oferecidas pelo Departamento de Informática (DI) da Ufes.

# <a name=“Mode-de-Execucao”><a/>Mode de Execução

### <a name=“Configuração”><a/>Configuração
No diretório raiz do repositório, acesse o arquivo **.env**

<div><img src="https://private-user-images.githubusercontent.com/56831082/283268851-7d5d1d91-30d5-4243-a67b-0cefc2507b23.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNjg4NTEtN2Q1ZDFkOTEtMzBkNS00MjQzLWE2N2ItMGNlZmMyNTA3YjIzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVmNGE2MTVmM2ZkMWM1YTcxMmM4Y2UxM2I3YzIyZTFjNjVmNWJjZDQyMzFkM2RjNWU4NTg2ODRjNjY3MmYzNmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.oxJognLWc4Zps74D_tzyqa32sXIMSit56qphP-sMONk" width=250> </div>

Neste arquivo, temos a configuração das portas em que os contêineres serão executados. Certifique-se de parar os contêineres do seu computador ou trocar as portas de acordo com a sua necessidade.

### <a name=“Execução”><a/>Execução
> **Windows**

**Intale o pip**
- https://pip.pypa.io/en/stable/installation/

**Rode o script**

- Dê um clique duplo no arquivo **run.bat**

> **Linux**

**Atualize o sistema**
```
sudo apt-get update && apt-get upgrade -y
```

**Instale o pip**
```
sudo apt install python3-pip
```

**Rode o script**
```
sh run.sh
```
Caso prefira, execute o comando diretamente
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.api.yml up -d --build
```

### <a name=“Visualizção”><a/>Visualizção
Para visualização do banco de dados, foi utilizado ao invés do Adminer, o pgAdmin, que é uma ferramenta gráfica de administração para o banco de dados PostgreSQL. Ele oferece uma interface visual para gerenciar e interagir com o PostgreSQL, incluindo recursos como navegação em árvore, edição SQL, gerenciamento de usuários e monitoramento de desempenho.

Para iniciar o pgAdmin, acesse a URL **localhost:5050** e faça o acesso com as credenciais abaixo:
- Login: admin@admin.com
- Senha: admin

<div Align="center"><img src="https://private-user-images.githubusercontent.com/56831082/283273405-1ec3213f-1536-4b50-84cb-48be7fe17226.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNzM0MDUtMWVjMzIxM2YtMTUzNi00YjUwLTg0Y2ItNDhiZTdmZTE3MjI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJlMmEwMDNlMzA1ZDI2ZmEyMmQ5YTRkZjdkMTQyOTYwYjBhZTQzYmJiMjI3ZDhhZDNhMmNkNzYwMTlkYzJiMTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.pUYdliOusIIxVGjrGPEL5coJtGfCo2ktZSmTTTFUoVs" width=550> </div>

Siga os passos abaixo para registrar o servidor

> ::::**_Click em add new serve_** ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: **_Defina um nome para o servidor_** ::::::::::::::::::::::::::::

|<img src="https://private-user-images.githubusercontent.com/56831082/283272421-751ee45e-04c9-4641-a85f-3f656d3bba9e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNzI0MjEtNzUxZWU0NWUtMDRjOS00NjQxLWE4NWYtM2Y2NTZkM2JiYTllLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4Y2YxN2JlOWU0ZDBjMGJiNDQ3ODBiYzdlYWE4NTNjMTBlNDFiNzRiZTE1ODZjMjc2YTE1NWJhNTVlYjJhMjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.KhX5ls6Ix7-M-Nuw7W-wrJoCxIFoRMos178IE2YVTm4" width=650><br> | <img  src="https://private-user-images.githubusercontent.com/56831082/283274759-c8c85ac1-6237-4447-aa51-6f0d36f8fa10.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNzQ3NTktYzhjODVhYzEtNjIzNy00NDQ3LWFhNTEtNmYwZDM2ZjhmYTEwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdmYTc1MjViNjljNjUzOGRmNDRlNWU0MWQ3ZjEwNmQyNWE5ZjhlYzQ4Nzg2YjkzYjYwNTNiYjFhYmFkYTE4YjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ixLZXiIdgp9zJgbXUkLtyaTX8vkPBqgD9oyO_bJ1A2k" width=500><br> |
| :---: | :---: |

> Acesse a aba Connection e finalize a configuração do servidor com os dados abaixo:

<div Align="center"><img src="https://private-user-images.githubusercontent.com/56831082/283277860-cca6eeb1-0e0a-448c-aee4-f5fcf22abd53.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyNzc4NjAtY2NhNmVlYjEtMGUwYS00NDhjLWFlZTQtZjVmY2YyMmFiZDUzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU5NjczMjA0OWJmMmVlMjU4YmM1MGMyODE3MzdhNjEwNzcwZmIyMmI2MTIwMTU1NTZhMDExZmM0OGY3ODc0MGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.eyU_v8xF5gXzWjHVhmzA0Wos1i8WNd-pCVxgnhl8RL8" width=450> </div>


# <a name=“Funcionamento”><a/>Funcionamento

O desenvolvimento do projeto se deu na criação de uma nova tabela `tagtable` para gerenciar tags para entidades do BOCA. Onde uma tag é uma espécie de rótulo que pode ser atribuído a qualquer entidade, para permitir categorizar os recursos.

Foi elaborado um conjunto de URLs a fim de se fazer a manipulação das tags, a elaboração da tabela pode ser observada pelo diagrama-ER conceitual abaixo:

<div Align="center"><img src="https://private-user-images.githubusercontent.com/56831082/283285354-f583658d-f8af-42b3-9c88-c71588b064aa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyODUzNTQtZjU4MzY1OGQtZjhhZi00MmIzLTljODgtYzcxNTg4YjA2NGFhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNjOGU4YzMzYzFiNjBkNjkxODcxNGY3NjAxNzQ0MmZlMTVhNzViMWMyNjU3YjFkZjhkOTU3YmFkZTRjZjg5NWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.JKUXdeOTZGvcpMIAQ-6TD-jpfuecvF_5iSMHHLvmUpc" width=600> </div>

Contudo, foi desenvolvida a seguinte tabela: 

<div Align="center"><img src="https://private-user-images.githubusercontent.com/56831082/283288633-54479ee9-e14d-45ed-9508-a2160d2e862a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMyODg2MzMtNTQ0NzllZTktZTE0ZC00NWVkLTk1MDgtYTIxNjBkMmU4NjJhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI4ZTkxNjI3OGMzOWJkZmU4YjgxYjNmYzVkMDg4YjYyMmU4MDI2MGU5NzQ5ZmVkZDgwMzhjMDk2ZTQyZDY2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.cw4_ojXMK2L4bfXo-5U5YHveXa2bsyI-K0naHHKjOgE" width=200> </div>

Com esta tabela, é possível relacionar a coluna `name` da tag com o respectivo `name` das tabelas (contest, lang, problem, site e user).

Foram desenvolvidas ao todo 5 URLs dinâmicas como vistas logo abaixo:

| Endpoint                                                               | Método  | Funcionalidade                                                       |
| ---------------------------------------------------------------------- | ------  | -------------------------------------------------------------------- |
| localhost:4040/api/**`entityType`**/**`entitynumber`**/tag             | GET     | Lista as tags associadas à entitytable dada pelo entitynumber        |
| localhost:4040/api/**`entityType`**/**`entitynumber`**/tag             | POST    | Cadastra uma nova tag associada à entitytable dada pelo entitynumber |
| localhost:4040/api/**`entityType`**/**`entitynumber`**/tag/**`tagId`** | GET     | Mostra a tag dada pelo tagId no entitytable entitynumber             |
| localhost:4040/api/**`entityType`**/**`entitynumber`**/tag/**`tagId`** | PUT     | Atualiza a tag dada pelo tagId no entitytable entitynumber           |
| localhost:4040/api/**`entityType`**/**`entitynumber`**/tag/**`tagId`** | DELETE  | Remove a tag dada pelo tagId no entitytable entitynumber             |

Na tabela a acima, encontramos três campos dinâmicos: `entityType`, `entityId` e `tagId`.

- `entityType`: Refere-se à entidade/tabela à qual a tag está associada. Por exemplo, se entityType for "user", isso se relaciona com a tabela usertable, que é a tabela referente aos usuários do sistema.

- `entityId`: Representa o ID da tupla na tabela da entidade. Por exemplo, se a entityType é user e o  entityId for 2, está referenciando o usuário cadastrado na tabela usertable com usernumber igual a 2.

- `tagId`: Faz referência a uma tag na tabela tagtable.

### <a name=“API”><a/>API 
A API desenvolvida foi construída utilizando o Flask em Python, um framework web leve que se destaca por sua simplicidade e extensibilidade. Classificado como um microframework, o Flask não impõe a necessidade de ferramentas ou bibliotecas específicas, mantendo um núcleo simples, porém flexível.

<div align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/c4306ec5-cfcb-4af5-95c9-47ab9be87709" width=450></div>
O código responsável pelo gerenciamento das URLs está organizado no arquivo controller.py, onde ocorre a interação com o banco de dados e a definição das rotas. Além disso, encontramos mais dois arquivos: run.py, encarregado de iniciar a API, rodando o codigo do controller via flask, e manufactures_connection, que realiza a conexão e configuração do banco de dados por meio das variáveis de ambiente.

### <a name=“Exemplos”><a/>Exemplos 

Para utilizar a API, você pode empregar ferramentas como o Postman, uma plataforma de colaboração para o desenvolvimento de APIs, ou desenvolver um código em Python para realizar as requisições. No repositório, você encontrará um arquivo **teste.py** com exemplos de requisições para a API.

A seguir, apresentamos alguns exemplos de chamadas de URL realizadas via `Postman`:

> **GET**

- Execução do GET
  
  ![GET](https://private-user-images.githubusercontent.com/56831082/283300032-fa3b2476-35c6-4ea4-8e07-59d97b36466c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDAwMzItZmEzYjI0NzYtMzVjNi00ZWE0LThlMDctNTlkOTdiMzY0NjZjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU0M2U0MjZiMDMxOGU0ZjU3M2I1NDc0Mjg0MTJlMjVmN2E3YTM1NDYyMTVkZTlkM2E0ZjFhNWE0Y2RjMTA1OTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.zqelo9xMfThmMneSY4GJRDFZbMb1sGz4ctfecDa8yIY)

Esta requisição retorna todas as tags associadas à tabela contest que possui constantnumbe igual a 2.

> **POST**

 - Execução do POST
   
   ![POST](https://private-user-images.githubusercontent.com/56831082/283301733-f1860c35-58cd-47b3-8763-b59afe45042e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDE3MzMtZjE4NjBjMzUtNThjZC00N2IzLTg3NjMtYjU5YWZlNDUwNDJlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBlY2Q2MjZkN2Y1MTIyMDU3OWM0YzA1MjFmNjJjMWFhOWEwMzE1MWUxZGMxNDYxMTRhMTFlNDVhOWRjMjdlOTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Sco-En301HOS-X4zkxp3jFECjbcpSdeosmgQO4JbnjQ)

Esta requisição registra uma nova tag na tabela tabtable para um contest existente que possui constantnumber igual a 2.

- Execução do GET após o POST para listar tags
  
  ![GET após POST](https://private-user-images.githubusercontent.com/56831082/283301964-0a7842bb-9435-4690-b85a-a30669a29ba1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDE5NjQtMGE3ODQyYmItOTQzNS00NjkwLWI4NWEtYTMwNjY5YTI5YmExLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE4YWRiODU1MmQzODEyZjA3ODc0ZTAzYTJmNjllZGNiNjM5ZjM5Y2RkMjA1YzFkMjZiZGZhZThmYjg0ZDA1MDQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.sKUM77tc65S3HTpo2Ph2OpYi-ndKubbYibXhvBmhzR0)

Mostra a alteração na lista de tags do contest.

> **GET**

- Execução do GET com presença do tagID
  
  ![GET com tagID](https://private-user-images.githubusercontent.com/56831082/283302903-187e20cd-fe4e-423b-86ab-90695fb51e06.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDI5MDMtMTg3ZTIwY2QtZmU0ZS00MjNiLTg2YWItOTA2OTVmYjUxZTA2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM1MzRjNjc3MjMyOWFkMjI1MzQzZDg5YmZiNjYzZmQ0MTg3YmRmMTgwYzRiMjk1OTkwYmMxZjcxYTNhMDE0MTEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.IIEvMzdPqoA1MWw8QzPAoISOzJjTCAKA-bVkLdkhsZw)

Exibe apenas a tag selecionada pelo id.

> **PUT**

- Executa PUT
  
  ![PUT](https://private-user-images.githubusercontent.com/56831082/283303192-eee856fe-9c3d-44fe-81bf-16a1c4b8e112.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDMxOTItZWVlODU2ZmUtOWMzZC00NGZlLTgxYmYtMTZhMWM0YjhlMTEyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRjZWQ1N2NmNzcwYTNkYzBlNmQwYzU2YjQ1Yjk0MDZjYTE4YjdiYWQwZDhkYmU0YjgwNTJiYzA2NzY1N2Y2NmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.B5EWDUy9mEJ8Ho4Mb8Y1RvP7SOabwd9bl4-XHxbnMQ8)

Altera a tag dada pelo tagID referente à tag da tabela tabtable para o contestnumber igual a 2. A alteração muda o valor de **"necessita revisão"** para **"revisado"**.

- Execução do GET com presença do tagID após o POST para listar a tag modificada
  
  ![GET após PUT](https://private-user-images.githubusercontent.com/56831082/283303240-01e082a2-84f7-42ff-b81d-d87ac9498793.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDMyNDAtMDFlMDgyYTItODRmNy00MmZmLWI4MWQtZDg3YWM5NDk4NzkzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNkMDk0ZDA2MzVmZTBiODEzZWIwMjdjNWI1OTMwNzdkZTMzOTA4NjJhZTFhNDZiZjQ3NjMyN2UxYmFiZjdhNDgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.HneUcBDlHTmOGNgWORSZct6_w5Ep4IcgboR9KGyLlEY)

Exibe apenas a tag selecionada pelo id, para denotar a alteração feita.

> **DELETE**

- Execução do DELETE
  
  ![DELETE](https://private-user-images.githubusercontent.com/56831082/283303831-b8065155-4a4a-47fc-9a1f-68cc27af56ab.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAxMDMwMzksIm5iZiI6MTcwMDEwMjczOSwicGF0aCI6Ii81NjgzMTA4Mi8yODMzMDM4MzEtYjgwNjUxNTUtNGE0YS00N2ZjLTlhMWYtNjhjYzI3YWY1NmFiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAyNDUzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIwY2ExYWRhM2RmZjc2ZTE1ODRhZTRhMTBlYmJkNzQzODU0OGVkZGZjYjI5MjhmMjUwZjAzODk5MDk5YjgzZDImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.6OZFs-3X-B59OmRHdBUH4_3LejbccelJai7S6AN3KqY)

Remove a tag da tabela tagtable.

> **Extra**

- Experimente remover tags para as quais o entitynumber da tabela entity não exista.
- Experimente listar tags que não foram registradas.
- Experimente alterar uma tag inexistente.
- Experimente fazer POST ou PUT sem os dados do JSON.
  
# Autores
| [<img src="https://avatars.githubusercontent.com/u/56831082?v=4" width=115><br><sub>Arthur Coelho Estevão</sub>](https://github.com/arthurcoelho442) |  [<img src="https://avatars.githubusercontent.com/u/56406192?v=4" width=115><br><sub>Milena da Silva Mantovanelli</sub>](https://github.com/Milena0899) |
| :---: | :---: |
</div>
