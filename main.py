# Import FastAPI framework to build API routes
from fastapi import FastAPI

# Import BaseModel from Pydantic to define and validate data models
from pydantic import BaseModel

# Create a FastAPI instance (your main app)
app = FastAPI()

# In-memory list to temporarily store todos (like a simple database)
todos = []

# Define the data model (schema) for a Todo item using Pydantic
class Todo(BaseModel):
    id: int                      # Unique ID for the todo (entered manually)
    title: str                   # Title of the todo
    completed: bool = False      # Completion status, defaults to False

# Define the home route (root URL) - basic welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}  # JSON response

# Create a new todo item
@app.post("/todos")
def create_todo(todo: Todo):              # Accepts a Todo object from the user(parameter: Class)
    todos.append(todo)                    # Adds the todo to the list
    return {"message": "Todo added", "todo": todo}  # Responds with a message and the added todo

# Return all todos
@app.get("/todos")
def get_todos():
    return todos                          # Returns the full list of todos

# Get a specific todo by its ID
@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):         # Receives the ID from the URL path
    for todo in todos:                    # Loops through all todos
        if todo.id == todo_id:            # If the ID matches, return that todo
            return todo
    return {"error": "Todo not found"}    # If not found, return an error

# Update an existing todo by its ID
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):  # Takes the ID from path and new data in body
    for index, todo in enumerate(todos):            # Loop through todos with index
        if todo.id == todo_id:                      # If the ID matches:
            updated_todo.id = todo_id               # Keep the original ID
            todos[index] = updated_todo             # Replace the old todo with the updated one
            return {"message": "Todo updated successfully", "todo": updated_todo}
    return {"error": "Todo not found"}              # If not found, return an error

# Delete a todo by its ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):            # Loop through todos with index
        if todo.id == todo_id:                      # If ID matches
            todos.pop(index)                        # Remove that todo from the list
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}              # If not found, return an error
