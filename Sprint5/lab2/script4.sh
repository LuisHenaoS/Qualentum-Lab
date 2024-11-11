#!/bin/bash

# credenciales database
DB_CREDENTIALS_FILE="/home/usersql/credentials_database.txt"

# verificamos
if [ -f "$DB_CREDENTIALS_FILE" ]; then
    source "$DB_CREDENTIALS_FILE"
else
    echo "El archivo $DB_CREDENTIALS_FILE no se encuentra."
    exit 1
fi

# verificamos
if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ] || [ -z "$DB_NAME" ]; then
    echo "completa todas las variables en $DB_CREDENTIALS_FILE"
    exit 1
fi

# Crear la base de datos y la tabla usando el usuario `usersql`
mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" <<EOF
CREATE DATABASE IF NOT EXISTS $DB_NAME;
USE $DB_NAME;
CREATE TABLE IF NOT EXISTS datos_servidor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(255) NOT NULL,
    cpu_usage_percent FLOAT,
    memory_total BIGINT,
    memory_available BIGINT,
    memory_used BIGINT,
    memory_used_percent FLOAT,
    system_uptime_seconds BIGINT,
    disk_total BIGINT,
    disk_free BIGINT,
    disk_used_percent FLOAT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF

echo "La base de datos y la tabla han sido inicializadas correctamente."

