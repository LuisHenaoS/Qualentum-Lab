#!/bin/bash

# creamos contraseñas aleatorias para cada usuario
USER_METRICS_PASS=$(openssl rand -base64 12)
USER_SQL_PASS=$(openssl rand -base64 12)

# creamos usuarios
sudo adduser --uid 9999 --disabled-password --gecos "" usermetrics
sudo adduser --uid 9998 --disabled-password --gecos "" usersql

# creamos un nuevo grupo de usuarios para los dos usuarios creados con permisos sudo
if ! getent group sudo_test > /dev/null; then
    sudo groupadd sudo_test
    echo "%sudo_test ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers
fi

sudo usermod -aG sudo_test usermetrics
sudo usermod -aG sudo_test usersql

# creamos directorios para cada script
sudo mkdir -p /opt/app1 /opt/app2

# guardamos las contraseñas generadas en el home de cada usuario
CREDENTIALS_FILE_USERMETRICS="/home/usermetrics/credentials.txt"
CREDENTIALS_FILE_USERSQL="/home/usersql/credentials.txt"

# guardamos las credenciales
sudo bash -c "cat > $CREDENTIALS_FILE_USERMETRICS" <<EOL
Usuario usermetrics - Contraseña: ${USER_METRICS_PASS}
EOL
sudo chown usermetrics:usermetrics $CREDENTIALS_FILE_USERMETRICS
sudo chmod 700 $CREDENTIALS_FILE_USERMETRICS

sudo bash -c "cat > $CREDENTIALS_FILE_USERSQL" <<EOL
Usuario usersql - Contraseña: ${USER_SQL_PASS}
EOL
sudo chown usersql:usersql $CREDENTIALS_FILE_USERSQL
sudo chmod 700 $CREDENTIALS_FILE_USERSQL

# creamos el archivo que maneja las credenciales de la base de datos en el home de usersql
DB_CREDENTIALS_FILE="/home/usersql/credentials_database.txt"
sudo bash -c "cat > $DB_CREDENTIALS_FILE" <<EOL

# completa manualmente con las credenciales de la base de datos

DB_HOST=localhost
DB_USER=
DB_PASS=
DB_NAME=metrics_db
EOL

# aseguramos permisos del archivo de credenciales de la base de datos
sudo chown usersql:usersql $DB_CREDENTIALS_FILE
sudo chmod 700 $DB_CREDENTIALS_FILE

echo "usuarios creados y sus credenciales guardadas en $CREDENTIALS_FILE_USERMETRICS y $CREDENTIALS_FILE_USERSQL"
