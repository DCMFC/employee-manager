# Use an official Python runtime as a parent image
FROM python:2.7.15

# Set the working directory to /employee-manager/magazine_luiza/
WORKDIR /employee-manager/magazine_luiza/

# Copy the current directory contents into the container at /app
COPY . /employee-manager/magazine_luiza/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME employee-manager

# Run app.py when the container launches
CMD ["python3", "manage.py"]
