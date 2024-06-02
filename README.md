# FastAPI REST API Project

This project introduces development in the FastAPI and Uvicorn frameworks. It covers topics such as HTTP methods, async await, user modeling, database usage, HTTP get, post, and delete requests, HTTP status codes, and raising exceptions. Furthermore, users can practice the concepts learned through hands-on exercises. By the end of this course, users will have a good understanding of the FastAPI and Uvicorn frameworks.

## Overview

This project demonstrates the creation of a RESTful API using FastAPI and Uvicorn. The API supports user management, including creating, retrieving, updating, and deleting users. Additionally, the project includes documentation using Swagger Docs and Redoc.

## Syllabus

1. Introduction to FastAPI and Uvicorn
2. Getting Started with FastAPI
3. HTTP Methods
4. Async Await
5. User Model
6. Database Integration
7. HTTP Get Requests
8. HTTP Post Requests
9. Rest Client Usage
10. Swagger Docs and Redoc
11. HTTP Delete Requests
12. HTTP Status Codes
13. Raising Exceptions
14. Hands-on Exercises

## Installation

To get started with this project, follow the steps below:

1. Clone the repository:

    ```sh
    git clone https://github.com/waqarmumtaz369/fastapi-rest-api-project.git
    cd fastapi-rest-api-project
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv fastenv
    source fastenv/bin/activate  # On Windows use `fastenv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:

    ```sh
    uvicorn main:app --reload
    ```

## Usage

Once the server is running, you can interact with the API using the following endpoints:

- **Root Endpoint:**
  - `GET /`: Returns a simple greeting message.

- **User Endpoints:**
  - `GET /api/v1/users`: Fetches all users.
  - `POST /api/v1/users`: Registers a new user.
  - `DELETE /api/v1/users/{user_id}`: Deletes a user by ID.
  - `PUT /api/v1/users/{user_id}`: Updates a user by ID.

## Example

Here's a brief example of how to interact with the API:

### Fetch all users

```sh
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/users' -H 'accept: application/json'


### Add a new user

```sh
curl -X 'POST' 'http://127.0.0.1:8000/api/v1/users' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "first_name": "Jane",
  "last_name": "Doe",
  "gender": "female",
  "roles": ["user"]
}'


### Delete a user

```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/api/v1/users/674c0976-5e1f-4f51-ade9-fc0d042e0d7f' -H 'accept: application/json'


### Update a user

```sh
curl -X 'PUT' 'http://127.0.0.1:8000/api/v1/users/674c0976-5e1f-4f51-ade9-fc0d042e0d7f' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "first_name": "Jane",
  "last_name": "Doe",
  "gender": "female",
  "roles": ["admin", "user"]
}'


## Documentation

API documentation is automatically generated and can be accessed at:

- **Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the Apache-2.0 License.