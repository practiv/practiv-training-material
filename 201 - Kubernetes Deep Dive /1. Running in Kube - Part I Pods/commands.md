# apply pod 
```bash
kubectl apply -f kubernetes/pod.yaml
```

# get pod
```bash
kubectl get pods
```

# tail pod logs
```bash
kubectl logs -f pod/flask-app
```

# port-forward to pod
```
kubectl port-forward pod/flask-app 8081:8080
```
