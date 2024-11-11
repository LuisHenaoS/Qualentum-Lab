#!/bin/bash

# damos permiso de ejecucion
chmod +x "$0"

# cada 3 minutos se ejecuta el script
CRON_JOB="*/3 * * * * usersql /opt/app2/script5.sh"

# añadimos a crontab
echo "$CRON_JOB" | sudo tee -a /etc/crontab

# reload
sudo systemctl restart cron

echo "cron añadido globalmente para ejecutarse cada 3 minutos"
