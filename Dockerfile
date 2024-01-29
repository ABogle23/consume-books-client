# Use an official Python runtime as a base image
FROM python:3.10.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=app/app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]


# To build 'docker buildx build --platform linux/amd64 -t ghcr.io/abogle23/consume-books-client:latest .'

# To run 'docker run -p 4999:5000 ghcr.io/abogle23/consume-books-client'

# To push to GHCR 'docker push ghcr.io/abogle23/consume-books-client:latest'