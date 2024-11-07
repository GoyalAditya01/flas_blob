# Use an official Python runtime as a parent image
FROM python:3.12-slim

# # Set environment variables to avoid Python buffering, which is useful for logging
# ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# # Install system dependencies
# RUN apt-get update && \
#     apt-get install -y gcc && \
#     rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "App_blob.py"]
