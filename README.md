Repo to show the pika consume issue. 

# Prerequisites 

docker and docker compose installed

# To reproduce

clone repo and run using `docker compose up`
To see different behaviour on different RabbitMQ's, uncomment the various images in the `docker-compose.yaml` file

on 3.12.2 and 3.12.10: 

```
python-app-1  |  [*] Waiting for messages:
python-app-1  |  [x] Received b'hello!'
python-app-1  |  Properties: {'x-delay': 1000L}
```
and on 3.13.0, 3.13.3 and 4.1.0(latest):

```
python-app-1  |  [*] Waiting for messages:
python-app-1  |  [x] Received b'hello!'
python-app-1  |  Properties: {'x-delay': 18446744073709550616L}
``` 


