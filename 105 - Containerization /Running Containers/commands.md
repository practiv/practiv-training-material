# running detached container
```bash
docker run -d flask-app:latest
``` 

# running container with port mapping
```bash
docker run -d -p 8080:8080 flask-app:latest
```

# getting container id
```bash
docker ps -a
```

# executing commands inside container

```bash
docker exec -it <container_id> bash
```
