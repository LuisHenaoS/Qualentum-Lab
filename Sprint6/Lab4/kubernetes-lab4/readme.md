## Kubernetes

Este proyecto despliega `Redis`, `app1` y `app2` en Kubernetes. El objetivo es realizar request a app2 y que nos devuelva el id de cada réplica. Balanceado y aleatorio.


### 1. Desplegar los Recursos en Kubernetes

Ejecuta los siguientes comandos:

1. Crea los recursos

```bash
kubectl apply -f redis.yaml
kubectl apply -f app1.yaml
kubectl apply -f app2.yaml 
```

2. Verifica de que todos los Pods estén Running y los servicios disponibles:

```bash
kubectl get pods
kubectl get services
```
![example](/Sprint6/Lab4/kubernetes-lab4/src/1.png)

3. Probar el Acceso Externo a app2
app2 está expuesto a través de un servicio de tipo NodePort en el puerto 30002. Puedes probar que app2 está funcionando ejecutando:


`curl -s http://localhost:30002`

![example](/Sprint6/Lab4/kubernetes-lab4/src/2.png)