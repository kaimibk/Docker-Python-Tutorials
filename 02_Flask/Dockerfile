# Set base image and version
FROM python:3.7

# Copy files to specific directories within the container
COPY ./app /app
COPY ./requirements /requirements

# Run the pip install command, and install the libraries specified
RUN pip install -r ./requirements/requirements.txt

# Set working directory in the container
WORKDIR /app

# Expose port 5000
EXPOSE 5000

# Command to run on container start
CMD ["python", "/app/main.py"]