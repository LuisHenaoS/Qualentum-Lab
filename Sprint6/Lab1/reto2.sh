#!/bin/bash

# rellena con las var
POSTGRES_DIR=~/postgres_data
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_DB=""

# creamos en home del user que ejecute el script
mkdir -p $POSTGRES_DIR

# ejecutamos el contenedor en el puerto 5432 del contenedor y host. Creara la database con las variables de entorno proporcionadas
docker run -d -p 5432:5432 -v $POSTGRES_DIR:/var/lib/postgresql/data --name lab2postgres -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -e POSTGRES_DB=$POSTGRES_DB postgres:15
