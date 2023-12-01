# Use an official Python runtime as a parent image
FROM python:3.13.0a2-alpine3.18

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (This step may not be necessary for your specific application)
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# (Modify this if your application listens on a different port)
EXPOSE 80

# Define environment variable
ENV NAME StringMatcherApp

# Run app.py when the container launches
CMD ["python", "main.py"]