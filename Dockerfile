# Use Python oficial image
FROM python:3.12-slim

# Define work directory in container
WORKDIR /app

# Copy files to the work directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expoxe flask connection port
EXPOSE 5000:5000

# Env variables from flask
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True
ENV FLASK_APP=app.app:create_app

# Init flask aplication
CMD ["flask", "run", "--host=0.0.0.0"]
