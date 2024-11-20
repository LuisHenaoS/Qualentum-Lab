#!/bin/bash

USER_NAME="" #define el nombre de tu user linux

if [ -z "$USER_NAME" ]; then
echo "[ERROR] Por favor, define el nombre de usuario en la variable USER_NAME."
  exit 1
fi

mkdir -p ~/nginx_content #creamos directamente en el home

echo "<h1>Hola $USER_NAME desde Nginx en Docker</h1>" > ~/nginx_content/index.html

docker run -d -p 12345:80 -v /home/$USER_NAME/nginx_content:/usr/share/nginx/html:ro --name lab1nginx nginx:1.25 #creamos con permiso de solo lectura