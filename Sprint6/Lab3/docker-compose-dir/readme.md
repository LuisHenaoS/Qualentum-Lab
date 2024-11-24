# balanceo de carga entre contenedores

- **En este ejercicio hago un balanceo de carga usando docker ayudándonos de Nginx.**

- Buscamos escalar app1 y app2 a cinco réplicas y situar por delante de app2 un balanceador de carga que se encargue de repartir el tráfico entre esas cinco instancias

- Con `docker-compose build` para la construcción de la iamagen y `docker-compose up -d` para levantarlo basta para probar la actividad.

# Recursos para el desarrollo de la actividad

En cada parte del código suministro la fuente donde fue encontrada la info. Como por ejemplo los deploy de los container(replicas) (https://docs.docker.com/reference/compose-file/deploy/#replicas). Simple de implementar e interesante lectura que da flexibilidad en el code.


# Manejo de errores

- Hubieron varios errores durante la creación de la actividad.

![example](/Sprint6/Lab3/docker-compose-dir/src/1.png)

1. puerto 5000 ocupado. Tan solo elminando la asignación de puertos de app2 se soluciona.

![example](/Sprint6/Lab3/docker-compose-dir/src/2.png)

2. nginx.conf necesitaba en el load balancer una sección de eventos. Fácil solución `https://nginx.org/en/docs/ngx_core_module.html#events`

![example](/Sprint6/Lab3/docker-compose-dir/src/3.png)


- Hubieron unos cuantos más errores previos pero olvidé documentar. Al final el ejercicio funciona:

![example](/Sprint6/Lab3/docker-composer-dir/src/4.png)