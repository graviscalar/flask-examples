# Quickstart

Simple Flask app with Docker

Exploring routes:

* default
* with GET and JSON return
* with POST and JSON data
* with GET, POST and JSON data

To build the Docker image, run the following command in the same directory as the Dockerfile
``` shell
 docker build -t flask_basic_docker .
```

To run the Docker container, run the following command:

``` shell
 docker run --name flask_basic_docker -p 5000:5000 flask_basic_docker
```

Enter the container to verify the saved images:
``` shell
 docker exec -ti flask_basic_docker sh
```


Test functionality by running the test.py
