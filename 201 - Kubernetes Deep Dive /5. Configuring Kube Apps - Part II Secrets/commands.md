# deploy secret from secret.yaml
```bash
kubectl apply -f kubernetes/secret.yaml
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

# base64ify your secret
```
cat kubernetes/license.json | base64
```
or
```
base65 -i kubernetes/license.json
```

# confirm you can decode the secret
```
echo "$YOUR_BASE64_STRING" | base64 -d
```
