# Microservico-Boca

<div  Align="justify">
<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/9e9c6b6a-24d3-4b3c-b3c0-fc4bd1733ded" height = 400 width=900> </div>

# Sumario
- [Objetivo do Trabalho](#Objetivo-do-Trabalho)
- [Mode de Execução](#Mode-de-Execucao)
  - [Configuração](#Configuracao)
  - [Execução](#Execucao)
  - [Visualização](#Visualizacao)
- [Funcionamento](#Funcionamento)
  - [Utilização](#Utilizacao)

# <a name=“Objetivo-do-Trabalho”><a/>Objetivo do Trabalho
Consiste no desenvolvimento de parte de um microsserviço de back-end que permite a aplicações clientes (por ex., front-end ou Application Programming Interface client) gerenciar turmas e objetos de aprendizagem armazenados em um SGBD através de uma API REST. Este trabalho oportuniza a prática dos conhecimentos obtidos na disciplina com tecnologias atuais e em um sistema real, o ambiente BOCA (BOCA Online Contest Administrator), o qual é usado para gerenciar competições da Maratona de Programação da SBC e do Topcom, e, mais recentemente, como ferramenta de apoio em disciplinas de programação oferecidas pelo Departamento de Informática (DI) da Ufes.

# <a name=“Mode-de-Execucao”><a/>Mode de Execução

### <a name=“Configuracao”><a/>Configuração
No diretório raiz do repositório, acesse o arquivo **.env**

<div><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/7d5d1d91-30d5-4243-a67b-0cefc2507b23" width=250> </div>

Neste arquivo, temos a configuração das portas em que os contêineres serão executados. Certifique-se de parar os contêineres do seu computador ou trocar as portas de acordo com a sua necessidade.

### <a name=“Execucao”><a/>Execução
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

### <a name=“Visualizacao”><a/>Visualização
Para visualização do banco de dados, foi utilizado ao invés do Adminer, o pgAdmin, que é uma ferramenta gráfica de administração para o banco de dados PostgreSQL. Ele oferece uma interface visual para gerenciar e interagir com o PostgreSQL, incluindo recursos como navegação em árvore, edição SQL, gerenciamento de usuários e monitoramento de desempenho.

Para iniciar o pgAdmin, acesse a URL **localhost:5050** e faça o acesso com as credenciais abaixo:
- Login: admin@admin.com
- Senha: admin

<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/1ec3213f-1536-4b50-84cb-48be7fe17226" width=550> </div>

Siga os passos abaixo para registrar o servidor

> ::::**_Click em add new serve_** ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: **_Defina um nome para o servidor_** ::::::::::::::::::::::::::::

|<img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/751ee45e-04c9-4641-a85f-3f656d3bba9e" width=650><br> | <img  src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/c8c85ac1-6237-4447-aa51-6f0d36f8fa10" width=500><br> |
| :---: | :---: |

> Acesse a aba Connection e finalize a configuração do servidor com os dados abaixo:

<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/cca6eeb1-0e0a-448c-aee4-f5fcf22abd53" width=450> </div>


# <a name=“Funcionamento”><a/>Funcionamento

O desenvolvimento do projeto se deu na criação de uma nova tabela `tagtable` para gerenciar tags para entidades do BOCA. Onde uma tag é uma espécie de rótulo que pode ser atribuído a qualquer entidade, para permitir categorizar os recursos.

Foi elaborado um conjunto de URLs a fim de se fazer a manipulação das tags, a elaboração da tabela pode ser observada pelo diagrama-ER conceitual abaixo:

<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/f583658d-f8af-42b3-9c88-c71588b064aa" width=600> </div>

Contudo, foi desenvolvida a seguinte tabela: 

<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/54479ee9-e14d-45ed-9508-a2160d2e862a" width=200> </div>

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

- `entityId`: Representa o ID da tupla na tabela da entidade. Por exemplo, se entityId for 2, está referenciando o usuário cadastrado na tabela usertable com usernumber igual a 2.

- `tagId`: Faz referência a uma tag na tabela tagtable.

### Utilização

Para utilizar a API, você pode empregar ferramentas como o Postman, uma plataforma de colaboração para o desenvolvimento de APIs, ou código em Python para realizar requisições. No repositório, você encontrará um arquivo **teste.py** com exemplos de requisições para a API.

A seguir, apresentamos alguns exemplos de chamadas de URL realizadas via `Postman`:

> **GET**

- Execução do GET
  
  ![GET](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/fa3b2476-35c6-4ea4-8e07-59d97b36466c)

Esta requisição retorna todas as tags associadas à tabela contest que possui constantnumbe = 2.

> **POST**

 - Execução do POST
   
   ![POST](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/f1860c35-58cd-47b3-8763-b59afe45042e)

Esta requisição registra uma nova tag na tabela tabtable para o contest com constantnumber = 2.

- Execução do GET após o POST para listar tags
  
  ![GET após POST](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/0a7842bb-9435-4690-b85a-a30669a29ba1)

Mostra a alteração na lista de tags do contest.

> **GET**

- Execução do GET com presença do tagID
  
  ![GET com tagID](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/187e20cd-fe4e-423b-86ab-90695fb51e06)

Exibe apenas a tag selecionada pelo id.

> **PUT**

- Executa PUT
  
  ![PUT](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/eee856fe-9c3d-44fe-81bf-16a1c4b8e112)

Altera a tag dada pelo tagID referente à tag da tabela tabtable para o contestnumber = 2. A alteração muda o valor de **"necessita revisão"** para **"revisado"**.

- Execução do GET com presença do tagID após o POST para listar a tag modificada
  
  ![GET após PUT](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/01e082a2-84f7-42ff-b81d-d87ac9498793)

Exibe apenas a tag selecionada pelo id, para denotar a alteração feita.

> **DELETE**

- Execução do DELETE
  
  ![DELETE](https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/b8065155-4a4a-47fc-9a1f-68cc27af56ab)

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
