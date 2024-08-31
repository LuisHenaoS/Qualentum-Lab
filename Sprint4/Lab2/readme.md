# Ejecución de Comandos en Máquinas Remotas mediante SSH

Este ejercicio consiste en configurar un entorno en el que puedas ejecutar comandos en máquinas remotas que están aisladas en redes privadas, accesibles únicamente a través de un bastion. El objetivo es establecer conexiones SSH sin contraseña para ejecutar comandos en `web1` y `web2` de manera eficiente y segura.

## Objetivo

El objetivo es configurar tu host para ejecutar comandos en los hosts `web1` y `web2` mediante SSH sin necesidad de contraseñas. Los hosts están en una red privada y son accesibles solo a través del bastion.

```bash
$ ssh web1.local hostname -a
web1
```

## Descripción de la Actividad

1. **Montar la Red de Pruebas**: Utilizando el `Vagrantfile` proporcionado, se crearán tres máquinas virtuales:
    - **bastion**: 192.168.19.100
    - **web1**: 192.168.19.101
    - **web2**: 192.168.19.102

2. **Generar Claves SSH**: Genera claves SSH y configura las máquinas para que `bastion` pueda acceder a `web1` y `web2` sin necesidad de contraseñas.

3. **Verificar la Configuración**: Asegúrate de que puedes ejecutar comandos en `web1` y `web2` desde `bastion` sin que se solicite una contraseña.

## Vagrantfile

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :
MACHINES = 2
BASTION_NETWORK_PREFIX = -> (i) { "192.168.19.#{i}" }

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  (1..MACHINES).each do |i|
    config.vm.define "web#{i}" do |web|
      web.vm.hostname = "web#{i}.local"

      web.vm.network "private_network", ip: "#{BASTION_NETWORK_PREFIX.call(i + 100)}"

      web.vm.provision :shell, inline: <<-SHELL
        iptables -A INPUT -s #{BASTION_NETWORK_PREFIX.call(0)}/24 -j ACCEPT
        iptables -A OUTPUT -d #{BASTION_NETWORK_PREFIX.call(0)}/24 -j ACCEPT
        iptables -A INPUT -j DROP
      SHELL

    end
  end

  config.vm.define "bastion" do |bastion|
    bastion.vm.hostname = "bastion.local"
    bastion.vm.network "private_network", ip: "#{BASTION_NETWORK_PREFIX.call(100)}"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end
end
```
