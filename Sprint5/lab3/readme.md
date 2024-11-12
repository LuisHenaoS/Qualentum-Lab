### Ejecución del Playbook

El entorno ha sido desde vsc conectado con wsl he desarrollado el ejercicio. Simplemente ejecutando el comando de abajo funciona sin problemas. 

![example](/Sprint5/lab3/source/1.png)

En la segunda ejecución sólo mostrará 1 changed.

![example](/Sprint5/lab3/source/2.png)


```bash
ansible-playbook -i inventory/hosts.yml playbooks/site.yml
```

Se ejecuta el playbook `site.yml` usando el inventario de `hosts.yml`.

### Descripción

El playbook realiza las siguientes tareas:
- Configura dos grupos de hosts: `db` y `ml`
- En el grupo `db` se instala nginx y se crea un usuario llamado `nginx`
- En el grupo `ml` se instala Python, pip, se crea un entorno virtual usando `virtualenv`, y se instala la librería `pandas`
