@echo off
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.api.yml up -d --build

@REM Adiciona um "pause" para aguardar a entrada do usuário
pause