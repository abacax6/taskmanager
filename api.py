from fastapi import FastAPI
from fastapi import HTTPException

from services import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task
)

app = FastAPI()

#Rotas
@app.get("/tasks")
def list_tasks():
    return get_all_tasks()

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    return get_task(task_id)

@app.post("/tasks")
def add_task(title: str, description: str):
    return create_task(title, description)

@app.patch("/tasks/{task_id}")
def change_status(task_id: int, status: str):
    return update_task(task_id, status)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)
