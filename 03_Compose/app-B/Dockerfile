# Set base image and version
FROM python:3.7

# Copy files to specific directories within the container
COPY . /app

# Run the pip install command, and install the libraries specified
RUN pip install -r .app/requirements/requirements.txt

# Set working directory in the container
WORKDIR /app

# Command to run on container start
CMD ["python", "main.py"]