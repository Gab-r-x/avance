# Use Python oficial image
FROM python:3.12-slim

# Define work directory in container
WORKDIR /app

# Copy requirements file to the work directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the application code
COPY . .

# Expose Flask connection port
EXPOSE 5000

# Env variables from Flask
ENV FLASK_ENV=development \
    FLASK_DEBUG=True \
    FLASK_APP=app.app:create_app

# Init Flask application
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
