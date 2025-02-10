# Build arguments
ARG NGINX_VERSION=1.27.4

# To override default argument value:
# $ docker build -t 05-dockerfile-arg:v1 --build-arg NGINX_VERSION=1.26 .

# Use nginx:alpine-slim as base image
FROM nginx:${NGINX_VERSION}-alpine-slim

# Custom labels
LABEL mantainer="Jhonattan Millán"
LABEL version="1.0"
LABEL description="A custom Docker image based on Nginx."
LABEL nginx_version ="${NGINX_VERSION}"

# OCI labels
LABEL org.opencontainers.image.authors="Jhonattan Millán"
LABEL org.opencontainers.image.title="My Nginx Alpine Image"
LABEL org.opencontainers.image.description="A custom Docker image based on nginx:alpine-slim."
LABEL org.opencontainers.image.version="1.0"

# Copy index.html file
COPY index.html /usr/share/nginx/html/index.html

