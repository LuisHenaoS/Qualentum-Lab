## Proyecto de Automatización y Monitoreo de Servidor

Este proyecto consiste en la configuración y automatización de un sistema de monitoreo para recolectar métricas de rendimiento del servidor utilizando una API en Flask, con almacenamiento de datos en una base de datos mariaDB y tareas cron para recolección periódica. Así como procesos demonio para que se ejecute todo en segundo plano de manera efectiva.

![example](/Sprint5/lab2/source/2.png)

## Estructura de Scripts

Para cada ejecución usa sudo bash: `sudo bash scriptX.sh`
 
1. **script1.sh** - Configura los usuarios `usermetrics` y `usersql` con sus permisos y credenciales iniciales en un .txt en su home. Crea un grupo sudo para ambos.
2. **script2.sh** - Configura los entornos virtuales de Python para ejecutar la API de monitoreo e instala dependencias y herramientas necesarias como `curl`, `jq`, y `mariadb`
3. **script3.txt** - Intrucciones en txt de cómo continuar y dónde logear. Configuramos el proceso demonio de la api así como configuramos su paradero (app.py)
4. **script4.sh** - crea la base de datos para almacenar las métricas.

    ### **Importante**:
   Una vez creada la database debemos darle permiso de uso a usersql desde root por configuraciones internas del primer uso de mariadb. El comando es `sudo mysql -u root -p` y después ejecutamos `CREATE USER IF NOT EXISTS 'usersql'@'localhost' IDENTIFIED BY '1234';  -- Asegúrate de que la contraseña coincide con la que está en `credentials_database.txt`
GRANT ALL PRIVILEGES ON *.* TO 'usersql'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;`
 
5. **script5.sh** - Script que realiza solicitudes a la API y almacena las métricas recolectadas en la base de datos previamente creada.
6. **script6.sh** - Script que crea una tarea cron global en `/etc/crontab` para ejecutar `script5.sh` cada 3 minutos.
7. **script7.txt** - Script que configura el daemon de la base de datos que gestiona si que esté siempre arriba aunque se reinicie el sistema o se use otro user, en `systemd`.


Sigue el orden para completar la configuración. Sobretodo si usas vagrant. Se puede seguir el orden directamente desde una máquina debian, si tienes las dependencias las obviará. Si usas vagrant descarga el archivo modificando la ruta compartida sync y tan solo debes ejecutar los scripts desde la carpeta que hayas proporcionado y contengas los archivos que te paso


---

