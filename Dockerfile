# Use a lightweight base image with Python 3.8
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the DNS port
EXPOSE 53/udp

# Command to run the application
CMD ["python", "dns_server.py"]
