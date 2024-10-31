## Flask con Gunicorn y Nginx en Vagrant

Este proyecto configura un entorno de desarrollo de una aplicación Flask. Mediante Gunicorn y gestionada con Nginx como gateway. Todo esto se hace dentro de una máquina virtual Vagrant para replicar un entorno de producción básico.

## Requisitos

- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

### Configuración de la Carpeta Compartida

En el archivo `Vagrantfile` proporcionado, configura la carpeta compartida para que puedas acceder a tus archivos dentro de la VM. La primera ruta es la carpeta en tu máquina local y la segunda es el destino en la VM. En mi caso es así. En el escritorio:

```ruby
config.vm.synced_folder "C:/Users/luiis/Desktop", "/home/vagrant/sync"
```

### Pasos para Ejecutar la Aplicación

1. **Levantar la máquina virtual**
   
   Inicia la vm desde vagrantfile:
   ```sh
   vagrant up
   ```

2. **Copiar la Aplicación**
   
   Dentro de la vm, copia el archivo donde hayas guardado app.py del proyecto desde la carpeta compartida a `/home/vagrant/` porque ahí están los certificados. En mi caso es así:
   ```sh
   cp /home/vagrant/sync/desktop/lab4_4/app.py /home/vagrant/
   ```

3. **Iniciar Nginx**
   
   Inicia el servicio Nginx:
   ```sh
   sudo systemctl start nginx
   ```

4. **Abre una Segunda Terminal para los Logs de Gunicorn**
   
   Abre una segunda terminal y accede a la máquina virtual:
   ```sh
   vagrant ssh
   ```
   Después inicia Gunicorn para poder visualizar los logs:
   ```sh
   gunicorn -b 0.0.0.0:8888 app:app --access-logfile -
   ```

5. **Pruebas HTTP y HTTPS**
   
   Desde la primera terminal (la misma en la que iniciaste Vagrant por primera vez), realiza las siguientes pruebas con `curl` para verificar que la configuración funciona correctamente:
   
   ```sh
   curl -I http://local.qualentum.org -k
   curl -I https://local.qualentum.org -k
   ```
