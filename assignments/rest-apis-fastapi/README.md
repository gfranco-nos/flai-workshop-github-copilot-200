# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python, practicing route definition, request handling, and returning JSON responses.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a few simple routes that return JSON data. You will define endpoints for listing and retrieving items.

#### Requirements
Completed program should:

- Install and import `fastapi` and `uvicorn`
- Create a FastAPI app instance
- Define a `GET /` route that returns a welcome message, e.g.:
  ```json
  { "message": "Welcome to my API!" }
  ```
- Define a `GET /items` route that returns a list of at least 3 items:
  ```json
  [
    { "id": 1, "name": "Pencil" },
    { "id": 2, "name": "Notebook" },
    { "id": 3, "name": "Ruler" }
  ]
  ```
- Run the app using `uvicorn` and verify the routes work in a browser or with `curl`


### 🛠️	Add a Dynamic Route and POST Endpoint

#### Description
Extend the API with a route that accepts a path parameter to retrieve a single item by ID, and a POST endpoint to add new items.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` route that returns the item matching the given ID, or a 404 response if not found:
  ```json
  { "id": 1, "name": "Pencil" }
  ```
- Define a `POST /items` route that accepts a JSON body with a `name` field and adds a new item to the list:
  ```json
  { "id": 4, "name": "Eraser" }
  ```
- Use a Pydantic model to validate the request body
- Return the newly created item with its assigned ID in the response
