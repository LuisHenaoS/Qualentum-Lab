# Proyecto de Infraestructura Virtualizada con Vagrant

Este proyecto utiliza Vagrant para gestionar varias máquinas virtuales (VM) que actúan como servidores web y un bastión que funciona como un balanceador de carga. 
La configuración de red y la gestión de las VM se realizan a través de scripts de aprovisionamiento.

## Requisitos Previos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes programas en tu máquina local:

1. [Vagrant](https://www.vagrantup.com/downloads) - Herramienta de gestión de máquinas virtuales.
2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - Proveedor de VM utilizado por Vagrant.

# Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- `Vagrantfile`: Define la configuración de las máquinas virtuales.
- `provision_bastion`: Script de aprovisionamiento para el bastión.
- `provision_web`: Script de aprovisionamiento para los servidores web.

Si no funciona bien recuerda dar permisos a los archivos -> chmod +x provision_web y chmod +x provision_bastion


En caso de error con el balanceador de carga del archivo `provision_web` ejecutar en terminal de manera manual el aprovisionamiento --> 
- `vagrant provision web1`
- `vagrant provision web2`
- `vagrant provision web3`
- `vagrant provision web4`
- `vagrant provision web5`

También cuenta con echo's para log de vagrant `export VAGRANT_LOG=debug`

Para probar conectividad del bastion:
- `vagrant ssh bastion`
- `curl http://web1`
- `curl http://web2`
- `curl http://web3`
- `curl http://web4`
- `curl http://web5`

 y el status de nginx: `sudo service nginx status`
