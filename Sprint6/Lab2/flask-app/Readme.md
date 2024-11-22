# Dockerización de un app flask

Este lab simula dos fases de un proyecto. 

- La primera una imagen(`Dockerfile.dev`) que nos interesa que funcione lo antes posible para probarla.
Ignorando optimización y peso.

- La segunda imagen (`Dockerfile.prod`) donde optimizaremos la imagen creada para que sea ligera y eficiente.
Aparte le pasaremos args para que sea más dinámica.

## Documentación:

- la mayor diferencia es en el peso.

![example](/Sprint6/Lab2/flask-app/src/3.png)



- El tiempo de instalación de la primera es alto.



![example](/Sprint6/Lab2/flask-app/src/1.png)



Comando para crear la primera imagen: 
    `docker build -f Dockerfile.dev -t flask-dev .`

- Comparado con la segunda se consigue un mejor tiempo de instalación.



![example](/Sprint6/Lab2/flask-app/src/2.png)



Los comandos para instalar la segunda imagen es:
    `docker build -f Dockerfile.prod --build-args EXPOSED_PORT=8000 -t flask-prod`. Requiere pasarle un arg.
Para construir el contenedor: 
    `docker run -e EXPOSED_PORT=8000 -p 8000:8000 -ti (imagen)` Podemos cambiar mediante variable de entorno el puerto.
Para que se pueda probar hay que definir el puerto (-p):



![example](/Sprint6/Lab2/flask-app/src/4.png)
