# Microservico-Boca

<div  Align="justify">
<div Align="center"><img src="https://github.com/arthurcoelho442/Microservico-Boca/assets/56831082/9e9c6b6a-24d3-4b3c-b3c0-fc4bd1733ded" height = 400 width=900> </div>

# Sumario
- [Objetivo do Trabalho](#Objetivo-do-Trabalho)
- [Funcionamento](#Funcionamento)
- [Mode de Execução](#Mode-de-Execucao)

# <a name=“Objetivo-do-Trabalho”><a/>Objetivo do Trabalho
Consiste no desenvolvimento de parte de um microsserviço de back-end que permite a aplicações clientes (por ex., front-end ou Application Programming Interface client) gerenciar turmas e objetos de aprendizagem armazenados em um SGBD através de uma API REST1. Este trabalho oportuniza a prática dos conhecimentos obtidos na disciplina com tecnologias atuais e em um sistema real, o ambiente BOCA (BOCA Online Contest Administrator), o qual é usado para gerenciar competições da Maratona de Programação da SBC2 e do Topcom3 e, mais recentemente, como ferramenta de apoio em disciplinas de programação oferecidas pelo Departamento de Informática (DI) da Ufes.

# <a name=“Mode-de-Execucao”><a/>Mode de Execução
> **Windows**
Intale o [pip](https://pip.pypa.io/en/stable/installation/)

> Linux
**Atualização do sistema**
```
sudo apt-get update && apt-get upgrade -y
```
**Rode o script**
de um click duplo no arquivo **run.bat**

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

# <a name=“Funcionamento”><a/>Funcionamento

# Autores
| [<img src="https://avatars.githubusercontent.com/u/56831082?v=4" width=115><br><sub>Arthur Coelho Estevão</sub>](https://github.com/arthurcoelho442) |  [<img src="https://avatars.githubusercontent.com/u/56406192?v=4" width=115><br><sub>Milena da Silva Mantovanelli</sub>](https://github.com/Milena0899) |
| :---: | :---: |

</div>
