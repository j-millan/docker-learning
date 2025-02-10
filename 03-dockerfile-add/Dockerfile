# Use nginx:alpine-slim as base image
FROM nginx:alpine-slim

# Custom labels
LABEL mantainer="Jhonattan Millán"
LABEL version="1.0"
LABEL description="A custom Docker image based on Nginx."

# OCI labels
LABEL org.opencontainers.image.authors="Jhonattan Millán"
LABEL org.opencontainers.image.title="My Nginx Alpine Image"
LABEL org.opencontainers.image.description="A custom Docker image based on nginx:alpine-slim."
LABEL org.opencontainers.image.version="1.0"

# Add HTML files
ADD html_files.tar.gz /usr/share/nginx/html/
