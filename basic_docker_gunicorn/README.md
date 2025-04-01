# Quickstart

Simple Flask app with Docker and Gunicorn

Exploring routes:

* default
* with GET and JSON return
* with POST and JSON data
* with GET, POST and JSON data
* POST image to Flask and save image

To build the Docker image, run the following command in the same directory as the Dockerfile
``` shell
 docker build -t flask_basic_docker_gunicorn .
```

To run the Docker container, run the following command:

``` shell
 docker run --name flask_basic_docker_gunicorn -p 5000:5000 flask_basic_docker_gunicorn
```

Enter the container to verify the saved images:
``` shell
 docker exec -ti flask_basic_docker_gunicorn sh
```


Test functionality by running the test.py
