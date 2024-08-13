## Basic task management system using FastAPI 

This is a simple task management backend built with FastAPI

## Getting Started

First, install dependencies:

```bash
pip install -r requirements.txt
```

Next, run the application:

```bash
uvicorn app:app
```
If the above command completed without any errors, then you can visit the http://localhost:8000/docs to view the Swagger documentation and start testing the API

You can login with the following credentials:

```json
{
  "email": "admin@test.com",
  "password": "test"
}
