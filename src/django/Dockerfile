# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
# COPY requirements.txt .

# Install dependenciesx
RUN pip install django

# Copy the rest of the application files to the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the Django app
CMD ["python", "manage.py", "runserver"]

