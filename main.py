from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from models import TaskDB
from schemas import TaskCreate, TaskUpdate

# Initialize FastAPI app
app = FastAPI()

# Serve static files (like favicon.ico) from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define constant for error message
TASK_NOT_FOUND = "Task not found"

# In-memory DB (for simplicity)
tasks = {}

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}

# Create a new task
@app.post("/tasks/", response_model=TaskDB)
def create_task(task: TaskCreate):
    task_id = len(tasks) + 1
    task_data = TaskDB(id=task_id, **task.dict())
    tasks[task_id] = task_data
    return task_data

# Get a task by ID
@app.get("/tasks/{task_id}", response_model=TaskDB)
def read_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=TASK_NOT_FOUND)
    return tasks[task_id]

# Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskDB)
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=TASK_NOT_FOUND)
    stored_task = tasks[task_id]
    updated_data = task.dict(exclude_unset=True)
    updated_task = stored_task.copy(update=updated_data)
    tasks[task_id] = updated_task
    return updated_task

# Delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=TASK_NOT_FOUND)
    del tasks[task_id]
    return {"message": "Task deleted"}
