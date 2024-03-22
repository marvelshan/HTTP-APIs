# HTTP APIs for Account and Password Management
![1200px-Flask_logo svg](https://github.com/marvelshan/HTTP-APIs/assets/140870617/54136f84-4e43-4afe-b4ac-792378cf69dc)

This repository contains a solution for managing user accounts and passwords through two RESTful HTTP APIs, implemented in Python. The solution includes a Docker containerized application that hosts the APIs, with data storage and appropriate error handling.

## **APIs Overview**

### **API 1: Create Account**

- **Method**: POST
- **Endpoint**: **`/signUp`**
- **Inputs**:
  - **`username`**: string (3-32 characters)
  - **`password`**: string (8-32 characters, with at least 1 uppercase letter, 1 lowercase letter, and 1 number)
- **Output**:
  - **`success`**: boolean
  - **`reason`**: string (if account creation fails)

### **API 2: Verify Account and Password**

- **Method**: POST
- **Endpoint**: **`/signIn`**
- **Inputs**:
  - **`username`**: string
  - **`password`**: string
- **Output**:
  - **`success`**: boolean
  - **`reason`**: string (if verification fails)

## **Solution Details**

1. **Implementation Language**: Python
2. **Error Handling**: Comprehensive error handling and input validation are implemented.
3. **Data Storage**: Utilizes appropriate data storage solutions.
4. **Docker Container**: Packaged into a Docker container.
5. **GitHub Repository**: Hosted on GitHub with source code.
6. **API Documentation**: Provided in this repository with clear instructions and sample request/response payloads.
7. **User Guide**: Detailed instructions on how to run the container with Docker are provided below.

## User guide

**1. docker-compose.yml**

```dockerfile
version: '3'

services:
  senao_project_db:
    image: zakilu/senao_project:latest
    ports:
      - "3307:3306"
    environment:
      MYSQL_ROOT_PASSWORD: "1234"

  senao_project_app:
    image: zakilu/senao_project:senao_latest
    ports:
      - "5000:5000"
    depends_on:
      - senao_project_db
    restart: always
    environment:
      DATABASE_URI: "mysql://root:1234@senao_project_db:3306/profile"
```

**2. Start the Docker Compose** Environment:

```bash
docker compose up -d
```

_This command uses Docker Compose to build and start the containers defined in the docker-compose.yml file. The -d flag runs containers in detached mode, meaning they will run in the background._

**3. Wait for 10 Seconds:**

_Allow some time for the containers to initialize and the Flask server to start running. Ten seconds should be sufficient for the server to be ready to accept requests._

**4. Send a POST Request to Sign Up:**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "username": "Flask14",
        "password": "testPassword1234"
      }' \
  http://localhost:5000/api/signUp
```

expected:
**{"success":true}**

_This curl command sends a POST request to the /api/signUp endpoint of the Flask server running locally. It includes JSON data with a username and password to sign up a new user. The -H flag sets the Content-Type header to application/json._

**5. Send a POST Request to Sign In:**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "username": "Flask14",
        "password": "testPassword1234"
      }' \
  http://localhost:5000/api/signIn
```

expected:
**{"success":true}**

_This curl command sends a POST request to the /api/signIn endpoint of the Flask server, attempting to sign in with the same username and password provided during sign-up._

**6. Close docker container**

```bash
docker compose down
```

## Coding Schedule

**3/14** Proof of Concept (POC) Python framework, and found some projects on the Internet and GitHub. Developed a sign-up API, wrote tests to cover it, and added error handling.

_Problem:_ Considering whether to use an ORM or directly use SQL syntax and a validation tool.

**3/15** Developed the sign-up API and wrote the API documentation. Researched YAML for Swagger.

**3/16-3/17** Encountered an issue with building the Python image. Used venv to create a virtual environment to solve this problem, and successfully resolved it.

[Issue: Cannot build Python image – failure at pip install requirements](https://stackoverflow.com/questions/70942357/cannot-build-python-image-failure-at-pip-install-requirements)

**3/18** Updated the Dockerfile and docker-compose.yml and wrote the coding schedule.

**3/19**
Upload Docker images to Docker Hub and write a user guide in the README.

---
