# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system dependencies for Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    # Install Chrome dependencies
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    # Clean up
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Define environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROME_DRIVER=/usr/local/bin/chromedriver

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scores.json file to the root of the container
COPY scores.json /scores.json

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=main_score.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
