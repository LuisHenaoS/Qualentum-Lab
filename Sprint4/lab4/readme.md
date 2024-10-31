# Proyecto Flask con Gunicorn y Nginx en Vagrant

Este proyecto guía la configuración de un entorno de desarrollo con una aplicación Flask, servida mediante Gunicorn y gestionada con Nginx. Todo esto se hace dentro de una máquina virtual Vagrant para replicar un entorno de producción básico.

## Requisitos

- [Vagrant](https://www.vagrantup.com/) instalado.
- [VirtualBox](https://www.virtualbox.org/) u otro proveedor compatible con Vagrant.

## Configuración de la Carpeta Compartida

En el archivo `Vagrantfile`, configura la carpeta compartida para que puedas acceder a tus archivos dentro de la VM. La primera ruta es la carpeta en tu máquina local y la segunda es el destino en la VM.

```ruby
config.vm.synced_folder "C:/Users/luiis/Desktop", "/home/vagrant/sync"
```

## Pasos para Ejecutar la Aplicación

1. **Levantar la máquina virtual**
   
   Inicia la máquina virtual ejecutando:
   ```sh
   vagrant up
   ```

2. **Copiar la Aplicación**
   
   Dentro de la máquina virtual, copia la carpeta de la aplicación desde la carpeta compartida a `/home/vagrant/`:
   ```sh
   cp /home/vagrant/sync/desktop/lab4_4/app.py /home/vagrant/
   ```

3. **Iniciar Nginx**
   
   Inicia el servicio Nginx:
   ```sh
   sudo systemctl start nginx
   ```

4. **Abrir una Segunda Terminal para los Logs de Gunicorn**
   
   Abre una segunda terminal y accede a la máquina virtual con:
   ```sh
   vagrant ssh
   ```
   Luego, inicia Gunicorn con el registro de accesos para poder visualizar los logs:
   ```sh
   gunicorn -b 0.0.0.0:8888 app:app --access-logfile -
   ```

5. **Realizar Pruebas de Peticiones HTTP y HTTPS**
   
   Desde la primera terminal (la misma en la que iniciaste Vagrant), realiza las siguientes pruebas con `curl` para verificar que la configuración funciona correctamente:
   
   ```sh
   curl -I http://local.qualentum.org -k
   curl -I https://local.qualentum.org -k
   ```

## Notas

- Asegúrate de tener configurados los certificados SSL en `/home/vagrant/` para poder realizar las peticiones HTTPS.
- La configuración de Nginx y Gunicorn está orientada a replicar un entorno de producción de manera local. Puedes ajustar la configuración según tus necesidades.

¡Espero que te sea útil!
