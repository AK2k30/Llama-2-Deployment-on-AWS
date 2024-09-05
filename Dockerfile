# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir gradio requests

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Run the application when the container launches
CMD ["python", "chatbot_app.py"]