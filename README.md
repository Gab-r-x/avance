# Avance

Backend REST API for the Avance platform, designed to help students practice and solve ENEM questions efficiently.

## Table of Contents
1. [Setup without Containers](#setup-without-containers)
2. [Setup with Docker](#setup-with-docker)
3. [Additional Notes](#additional-notes)

---

### Setup without Containers

To run the application locally without using Docker, follow these steps:

1. **Create a Python Virtual Environment**
   ```bash
   virtualenv venv
   ```
   - **Note**: If you are using Python 3.12, run:
     ```bash
     python3.12 -m venv venv
     ```

2. **Activate the Virtual Environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   make install
   ```

4. **Set Up the Database**
   ```bash
   flask create-db
   ```

5. **Run the Application**
   ```bash
   flask run
   ```

---

### Setup with Docker

To run the application in Docker containers:

1. **Create a Python Virtual Environment**
   ```bash
   virtualenv venv
   ```
   - **Note**: For Python 3.12, use:
     ```bash
     python3.12 -m venv venv
     ```

2. **Activate the Virtual Environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   make install
   ```

4. **Build and Start Docker Containers**
   ```bash
   docker-compose up --build
   ```

5. **Initialize the Database in Docker**
   ```bash
   docker-compose exec flask_app flask create-db
   ```

---

### Additional Notes

- **Dependencies**: Ensure all dependencies are listed in `requirements.txt`.
- **Database Creation**: For the initial database setup, `flask create-db` is essential.
- **Environment Variables**: Confirm that environment variables are correctly configured for both local and Docker environments.
  
---