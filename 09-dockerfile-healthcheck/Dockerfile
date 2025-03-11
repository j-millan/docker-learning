# Use alpine as base image
FROM nginx:alpine-slim

# OCI labels
LABEL org.opencontainers.image.authors="Jhonattan Millán"
LABEL org.opencontainers.image.title="Healtcheck Demo"
LABEL org.opencontainers.image.description="A custom Docker image to illustrate the usage of HEALTHCHECK instruction."
LABEL org.opencontainers.image.version="1.0"

# Install curl
RUN apk --no-cache add curl


# Copy html file
COPY index.html /usr/share/nginx/html/index.html

# Expose the port
EXPOSE 80

# Define healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --start-interval=5s --retries=3 CMD curl -f http://localhost:80 || exit 1

# Build the image
# $ docker build -t healthcheck-demo:v1 .

# Inspect the image to verify healthcheck config
# $ docker image inspect healthcheck-demo:v1 --format='{{json .Config.Healthcheck}}'