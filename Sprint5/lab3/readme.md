### Ejecución del Playbook

El entorno ha sido desde vsc conectado con wsl he desarrollado el ejercicio. Simplemente ejecutando el comando de abajo funciona sin problemas. En la segunda ejecucón sólo mostrará 1 changed.

```bash
ansible-playbook -i inventory/hosts.yml playbooks/site.yml
```

Se ejecuta el playbook `site.yml` usando el inventario de `hosts.yml`.

### Descripción

El playbook realiza las siguientes tareas:
- Configura dos grupos de hosts: `db` y `ml`
- En el grupo `db` se instala nginx y se crea un usuario llamado `nginx`
- En el grupo `ml` se instala Python, pip, se crea un entorno virtual usando `virtualenv`, y se instala la librería `pandas`
