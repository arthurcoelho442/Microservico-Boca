#!/bin/bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.api.yml up -d --build

# Adiciona um "wait for enter"
read -p "Pressione Enter para finalizar..."