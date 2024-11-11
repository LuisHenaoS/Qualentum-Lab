#!/bin/bash

# guarda o copia este script en /opt/app2 estando en usersql

# GET a app.py y lo guarda en formato JSON_DATA
JSON_DATA=$(curl -s http://localhost:5000/metrics)

DB_CREDENTIALS_FILE="/home/usersql/credentials_database.txt"

if [ -f "$DB_CREDENTIALS_FILE" ]; then
    source "$DB_CREDENTIALS_FILE"
else
    echo "El archivo $DB_CREDENTIALS_FILE no se encuentra. Por favor, créelo y complete las credenciales."
    exit 1
fi

JSON_DATA=$(curl -s http://localhost:5000/metrics)

# usamos jq para el manejo de JSON
CPU_USAGE=$(echo $JSON_DATA | jq -r '.cpu_usage_percent')
MEMORY_TOTAL=$(echo $JSON_DATA | jq -r '.memory_total')
MEMORY_AVAILABLE=$(echo $JSON_DATA | jq -r '.memory_available')
MEMORY_USED=$(echo $JSON_DATA | jq -r '.memory_used')
MEMORY_USED_PERCENT=$(echo $JSON_DATA | jq -r '.memory_used_percent')
SYSTEM_UPTIME=$(echo $JSON_DATA | jq -r '.system_uptime_seconds')
HOSTNAME=$(echo $JSON_DATA | jq -r '.system_hostname')
DISK_TOTAL=$(echo $JSON_DATA | jq -r '.disk_total')
DISK_FREE=$(echo $JSON_DATA | jq -r '.disk_free')
DISK_USED_PERCENT=$(echo $JSON_DATA | jq -r '.disk_used_percent')

# guardamos los datos en la base de datos
mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -D "$DB_NAME" <<EOF
INSERT INTO datos_servidor (hostname, cpu_usage_percent, memory_total, memory_available, memory_used, memory_used_percent, system_uptime_seconds, disk_total, disk_free, disk_used_percent, fecha) VALUES 
('$HOSTNAME', $CPU_USAGE, $MEMORY_TOTAL, $MEMORY_AVAILABLE, $MEMORY_USED, $MEMORY_USED_PERCENT, $SYSTEM_UPTIME, $DISK_TOTAL, $DISK_FREE, $DISK_USED_PERCENT, NOW());
EOF

echo "Base de datos actualizada"