# Set base image and version
FROM python:3.7

# Copy files to specific directories within the container
COPY ./app /app

# Set working directory in the container
WORKDIR /app

# Command to run on container start
CMD ["python", "/app/main.py"]