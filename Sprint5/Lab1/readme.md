# Autodeps

Autodeps es un script en bash que gestiona las dependencias de proyectos específicos al detectar archivos como `pom.xml`, `build.gradle` y `requirements.txt`. Diseñado para ejecutarse en un entorno Debian.

*Copia el archivo `autodeps`* en `/usr/local/bin` (en mi caso) o en cualquier directorio de tu `$PATH`
   ```bash
   sudo cp autodeps /usr/local/bin
   sudo chmod +x /usr/local/bin/autodeps
   ```
*Agrega el archivo `.bashrc` dado a tu `~/.bashrc`* para que al ejecutar `cd` se ejecute autodeps. Después ejecuta ` source ~/.bashrc` para actualizar
   ```bash
   .bashrc > ~/.bashrc
   source ~/.bashrc
   ```

Autodeps se activará automáticamente cuando entres en un directorio que contenga uno de los archivos detectables (`pom.xml`, `build.gradle`, o `requirements.txt`).


# Opciones de Control

- *Desactivar con una variable de entorno*: Puedes exportar la variable `_AUTODEPS_DISABLE_AUTO_DOWNLOAD` para desactivar autodeps temporalmente.
  ```bash
  export _AUTODEPS_DISABLE_AUTO_DOWNLOAD=1
  ```

- *Archivo de bloqueo*: Crea `.lock_autodeps` en el directorio actual para bloquear la ejecución de `autodeps`.
  ```bash
  touch .lock_autodeps
  ```

- *Control de tiempo*: Si `autodeps` se ejecutó en el último periodo de una hora, no intentará instalar dependencias nuevamente.
