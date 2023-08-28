# Use a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
COPY . /app

# Install any dependencies required by your mini project
RUN pip install -r requirements.txt

# Set the notes directory as the working directory for the mini project
WORKDIR /app/notes

# Specify the command to run your mini project
CMD python /app/app/Mini_project3_in_progress.py