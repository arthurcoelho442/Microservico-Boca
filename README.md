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

# <a name=“Objetivo-do-Trabalho”><a/>Objetivo do Trabalho
Consiste no desenvolvimento de parte de um microsserviço de back-end que permite a aplicações clientes (por ex., front-end ou Application Programming Interface client) gerenciar turmas e objetos de aprendizagem armazenados em um SGBD através de uma API REST1. Este trabalho oportuniza a prática dos conhecimentos obtidos na disciplina com tecnologias atuais e em um sistema real, o ambiente BOCA (BOCA Online Contest Administrator), o qual é usado para gerenciar competições da Maratona de Programação da SBC2 e do Topcom3 e, mais recentemente, como ferramenta de apoio em disciplinas de programação oferecidas pelo Departamento de Informática (DI) da Ufes.

# <a name=“Mode-de-Execucao”><a/>Mode de Execução

### <a name=“Configuracao”><a/>Configuração
No diretorio raiz do repositorio acesse o arquivo **.env**

<div><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/7d5d1d91-30d5-4243-a67b-0cefc2507b23" width=250> </div>

neste arquivo temos a configuração das portas em que os conteiners seram executados, certifique de parar os containers do seu compudator ou trocar as portas de acordo com a sua necessidade.

### <a name=“Execucao”><a/>Execução
> **Windows**

**Intale o pip**
- https://pip.pypa.io/en/stable/installation/

**Rode o script**

- De um click duplo no arquivo **run.bat**

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
caso prefira execute o comando diretamente
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.api.yml up -d --build
```

### <a name=“Visualizacao”><a/>Visualização
Para visualização do banco de dados, foi utilizado ao invez do adminer, o pgadmin que é uma ferramenta gráfica de administração para o banco de dados PostgreSQL. Ele oferece uma interface visual para gerenciar e interagir com o PostgreSQL, incluindo recursos como navegação em árvore, edição SQL, gerenciamento de usuários e monitoramento de desempenho.

Para iniciar o pgadmin acesse a url **localhost:5050** e faça o acesso com as credenciais abaixo:
- login: admin@admin.com
- senha: admin

<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/1ec3213f-1536-4b50-84cb-48be7fe17226" width=550> </div>

Siga os passos abaixo para registrar o servidor

> ::::**_Click em add new serve_** ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: **_Defina um nome para o servidor_**::::::::::::::::::::::::::

|<img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/751ee45e-04c9-4641-a85f-3f656d3bba9e" width=650><br> | <img  src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/c8c85ac1-6237-4447-aa51-6f0d36f8fa10" width=500><br> |
| :---: | :---: |

# <a name=“Funcionamento”><a/>Funcionamento

# Autores
| [<img src="https://avatars.githubusercontent.com/u/56831082?v=4" width=115><br><sub>Arthur Coelho Estevão</sub>](https://github.com/arthurcoelho442) |  [<img src="https://avatars.githubusercontent.com/u/56406192?v=4" width=115><br><sub>Milena da Silva Mantovanelli</sub>](https://github.com/Milena0899) |
| :---: | :---: |

</div>
