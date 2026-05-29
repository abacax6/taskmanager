from fastapi import FastAPI
from fastapi import Response
from fastapi import HTTPException
from schemas import ( 
    TaskUpdate, 
    TaskStatus, 
    TaskCreate, 
    TaskResponse
)
from services import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task
)

app = FastAPI()

#Rotas
@app.get("/tasks", response_model=list[TaskResponse]) #GET ALL
def list_tasks(q: str | None = None, status: TaskStatus | None = None):
    tasks = get_all_tasks(q, status)

    if not tasks:
        return Response(status_code=204)

    return tasks

@app.get("/tasks/{task_id}") #GET
def read_task(task_id: int):
    try:
        return get_task(task_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/tasks", response_model=TaskResponse, status_code=201) #POST
def add_task(task: TaskCreate):
    try:
        return create_task(task.title, task.description)
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.patch("/tasks/{task_id}") #PATCH
def update(task_id: int, task_data: TaskUpdate):
    try:
        return update_task(task_id, task_data)
        
    except ValueError as e:
        message = str(e)

        if message == "Task not found":
            raise HTTPException(status_code=404, detail = message)
        
        raise HTTPException(status_code=400, detail = message)

@app.delete("/tasks/{task_id}") #DELETE
def remove_task(task_id: int):
    try:
        delete_task(task_id)
        return Response(status_code=204)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
