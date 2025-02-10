# Build arguments
ARG NGINX_VERSION=1.27.4

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

# Copy nginx ocnfiguration files
COPY nginx-conf/*.conf /etc/nginx/conf.d/

# Copy index.html file
COPY html/*.html /usr/share/nginx/html/

# Add curl package using RUN
RUN apk --no-cache add curl

# Expose ports 8081, 8082 and 8083
EXPOSE 8081 8082 8083