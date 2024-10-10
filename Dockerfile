# Use a base image with Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Ensure Python is installed correctly
RUN python3 --version

# Make port 80 available to the world outside this container
EXPOSE 800 8080

# Run bot.py when the container launches
# CMD ["/usr/local/bin/python", "bot.py"]
CMD ["python3", "bot.py"]
# CMD ["bin/python3", "bot.py"]

