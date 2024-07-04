# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask selenium

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg2
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
RUN wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin/

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches
CMD ["python", "app.py"]