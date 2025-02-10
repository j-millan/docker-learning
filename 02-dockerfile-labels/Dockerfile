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
LABEL org.opencontainers.image.created="2024-16-01T12:20:00"
LABEL org.opencontainers.image.url=""
LABEL org.opencontainers.image.source=""
LABEL org.opencontainers.image.documentation=""
LABEL org.opencontainers.image.vendor="JHONATTAN M."
LABEL org.opencontainers.image.licenses=""

# Insert custom html
COPY index.html /usr/share/nginx/html/index.html
