# Python version build-time argument
ARG PYTHON_VERSION=3.12.4

# Use python:alpine as base image
FROM python:${PYTHON_VERSION}-alpine

# Custom labels
LABEL mantainer="Jhonattan Millán"
LABEL version="1.0"
LABEL description="A Dockerfile demo showing the usage of ARG and ENV instructions."
LABEL python_version="${PYTHON_VERSION}"

# OCI labels
LABEL org.opencontainers.image.authors="Jhonattan Millán"
LABEL org.opencontainers.image.title="Dockerfile ARG and ENV"
LABEL org.opencontainers.image.description="A Dockerfile demo showing the usage of ARG and ENV instructions."
LABEL org.opencontainers.image.version="1.0"

# Environment build-time argument
ARG ENVIRONMENT=dev

# Runtime environment variables
ENV APP_ENVIRONMENT=${ENVIRONMENT}

# Set the working directory
WORKDIR /app

# Copy package requirements
COPY requirements.txt .

# Install package dependencies
RUN pip install -r requirements.txt

# Copy app source code
COPY app.py .

# Copy templates
COPY templates ./templates/

RUN echo "Building for environment: ${APP_ENVIRONMENT}"

# Expose ports 80
EXPOSE 80

# Start the python app as entrypoint
CMD ["python", "app.py"]
