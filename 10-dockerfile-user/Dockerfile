# Use python:alpine as base image
FROM python

# OCI labels
LABEL org.opencontainers.image.authors="Jhonattan Millán"
LABEL org.opencontainers.image.title="Dockerfile USER instruction"
LABEL org.opencontainers.image.description="A Dockerfile demo to illustrate the usage of the USER instruction."
LABEL org.opencontainers.image.version="1.0"

# Set the working directory
WORKDIR /usr/src/app

# Copy package requirements
COPY requirements.txt .

# Install package dependencies
RUN pip install -r requirements.txt

# Copy app source code
COPY app.py .

# Define environmnet variables for user and group
ENV USER=myuser
ENV GROUP=mygroup

# Create group 'myuser' and add non-root user 'myuser' to this group
RUN groupadd ${GROUP} && useradd -m -r -g ${GROUP} ${USER}

# Set the ownership of the '/usr/src/app' directory to the user 'myuser'
RUN chown -R ${USER}:${GROUP} /usr/src/app

# Switch to the new user 'myuser' for the rest of the build stage
USER ${USER}

# Expose ports 5000
EXPOSE 5000

# Start the python app as entrypoint
CMD ["python", "app.py"]
