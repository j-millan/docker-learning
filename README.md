#### This project was made following [this course](https://www.udemy.com/course/docker-in-a-weekend-40-practical-demos-for-devops-learners/?srsltid=AfmBOoritFZZ9_0x6gHY1hwWs1rxj7URL9nf1RLa6OCZF5vEC_9z5U0s&couponCode=LETSLEARNNOW).


## Command examples:

### Build the image with default ARG values
```bash
$ docker build -t my-image:v1 .
```

### Build the image overriding default ARG values
```bash
$ docker build -t my-image:v1 . --build-arg PYTHON_VERSION=3.4.5 --build-arg ENVIRONMENT=qa
```

### Run the container overriding default environment variables
```bash
$ docker run --name my-container -e APP_ENVIRONMENT=qa -p 8080:80 -d my-image:v1
```

### Inspect docker image
```bash
$ docker image inspect my-container --format='{{.Config}}'
```

### Remove all docker containers
```bash
$ docker rm -f $(docker ps -aq)
```

### Remove all docker images
```bash
$ docker rmi $(docker images -q)
```

### Override image ENTRYPOINT when running container
```bash
$ docker run --name my-image --entrypoint /bin/sh my-image:v1 -c "COMMAND HERE"
```
