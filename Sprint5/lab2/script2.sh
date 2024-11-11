#!/bin/bash

# actualizamos e instalamos Python y venv globalmente si es necesario
sudo apt-get update
if ! command -v python3 &> /dev/null; then
    sudo apt-get install -y python3
fi

# verificamos e instalamos python3-venv para crear entornos virtuales
if ! dpkg -s python3-venv &> /dev/null; then
    sudo apt-get install -y python3-venv
fi

# instalamos curl si no está disponible
if ! command -v curl &> /dev/null; then
    sudo apt-get install -y curl
else
    echo "curl ya está instalado."
fi

# instalamos jq si no está disponible
if ! command -v jq &> /dev/null; then
    sudo apt-get install -y jq
else
    echo "jq ya está instalado."
fi

# instalamos MariaDB
if ! command -v mariadb-server &> /dev/null; then
    sudo apt-get install -y mariadb-server
else
    echo "MariaDB ya está instalado."
fi

# creamos el entorno virtual en app1 para usermetrics
sudo python3 -m venv /opt/app1/env

# verificamos pip (por errores surgidos en pruebas)
if [ ! -f /opt/app1/env/bin/pip ]; then
    sudo /opt/app1/env/bin/python3 -m ensurepip --upgrade
    sudo /opt/app1/env/bin/pip install --upgrade pip
fi

# requirements.txt con gunicorn y psutil
cat > /opt/app1/requirements.txt <<EOL
gunicorn
psutil
flask
EOL

# instalamos los requirements
sudo /opt/app1/env/bin/pip install -r /opt/app1/requirements.txt

# permisos de la carpeta app1 solo para usermetrics (solo él lo gestionará)
sudo chown 9999:9999 /opt/app1
sudo chmod 700 /opt/app1

# permisos de la carpeta app2 solo para usersql
sudo chown 9998:9998 /opt/app2
sudo chmod 700 /opt/app2

echo "Permisos configurados en usermetrics y usersql"