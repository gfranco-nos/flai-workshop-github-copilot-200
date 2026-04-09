from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Sample data ---
items = [
    {"id": 1, "name": "Pencil"},
    {"id": 2, "name": "Notebook"},
    {"id": 3, "name": "Ruler"},
]


# --- Pydantic model for request body ---
class ItemCreate(BaseModel):
    name: str


# --- Task 1: Basic routes ---

# TODO: Define a GET / route that returns a welcome message


# TODO: Define a GET /items route that returns the list of items


# --- Task 2: Dynamic route and POST endpoint ---

# TODO: Define a GET /items/{item_id} route that returns the item with the given ID
#       Return a 404 error if the item is not found


# TODO: Define a POST /items route that accepts an ItemCreate body,
#       adds a new item to the list with a unique ID, and returns the created item


# --- Run the app ---
# To start the server, run from your terminal:
#   uvicorn starter-code:app --reload
