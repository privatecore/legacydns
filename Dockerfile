# Use a lightweight base image with Python 3.8
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the DNS port
EXPOSE 53/udp

# Command to run the application
CMD ["python", "main.py"]
