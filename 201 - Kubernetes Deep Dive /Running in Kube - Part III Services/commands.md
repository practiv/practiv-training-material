# apply deployment and service 
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

# get service
```bash
kubectl get service
```
# port-forward to localhost 
```bash
kubectl port-forward service/flask-app-service 8080:80
```

# get all of our pods for flask-app
```bash
kubectl get pods -l app=flask-app
```

# tail the logs of all the pods
```bash
kubectl logs -l app=flask-app -f
```
