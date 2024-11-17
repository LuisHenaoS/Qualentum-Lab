# Configuración de WordPress, apache, nginx y creación de database con Ansible y Vagrant

Este proyecto utiliza Ansible y Vagrant para desplegar un entorno de WordPress en máquinas virtuales. Está diseñado para automatizar el aprovisionamiento y configuración de los nodos necesarios para la instalación. 

Crea también una base de datos con el usuario root y un usuario correspondiente al nodo 3 que tendrá acceso a gestionar la database. Esto se hace con los datos proporcionados en el archivo /vars/. Nginx se encargará de distribuir el tráfico mediante un reverse proxy. Apache se configura también y complementa nuestro stack LAMP.

Se pueden hacer todo de pruebas entrando en cada nodo. Recuerda la distribución: `nodo1.example.com` y `nodo2.example.com` gestionan la web. Tienen un user en apache que podrás modificar en /vars/web.yaml, así como el puerto si así se desea.

`nodo3.example.com` está destinado a la database. El usuario también es configurado a gusto.

`installer` es el nodo que se encarga de instalar todo mediante ansible. También es el nodo encargado de gestionar nginx.


**Ejecuta `vagrant up` y se aprovisionará todo.** 

Una vez levantado se puede hacer todo tipo de pruebas como peticiones, entrar a la database, modificar el tráfico.. Pero todo en su correspondiente nodo. 


![example](/Sprint5/Lab4/source/1.png)


Se puede lanzar tanto desde windows como desde linux.


**Importante**: Necesitarás rellenar las variables restantes. Situadas en `/ansible_wordpress/vars/db.yaml y web.yaml`
