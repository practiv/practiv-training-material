# build the docker image with our new tag

```bash
docker build -t flask-app:latest-config . 
```

# create config map from config.json 
```bash
kubectl create configmap greeting-config --from-file=config.json
```

or 

# deploy config map from config.yaml
```bash
kubectl apply -f kubernetes/configmap.yaml
```

or 

# apply all services under /kubernetes
```bash
kubectl apply -f kubernetes/
```

# port-forward to localhost
```bash
kubectl port-forward service/flask-app-service 8080:80
```

# exec inside pod container to view filesystem and verify config is mounted correctly
```bash
kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
```
