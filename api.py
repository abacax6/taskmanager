from fastapi import (
    FastAPI,
    Response,
    HTTPException
)
from schemas import ( 
    TaskUpdate, 
    TaskStatus, 
    TaskCreate, 
    TaskResponse,
    UserLogin,
    UserCreate,
    UserResponse
)
from services import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task,
    create_user
)
from auth import (
    authenticate_user,
    create_access_token
)

app = FastAPI()

#Rotas
@app.get("/tasks", response_model=list[TaskResponse]) #GET ALL
def list_tasks(q: str | None = None, status: TaskStatus | None = None):
    tasks = get_all_tasks(q, status)

    if not tasks:
        return Response(status_code=204)

    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse) #GET
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

@app.patch("/tasks/{task_id}", response_model=TaskResponse) #PATCH
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

@app.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate
):

    try:

        return create_user(
            user.email,
            user.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.post("/login")
def login(credentials: UserLogin):

    try:

        user = authenticate_user(
            credentials.email,
            credentials.password
        )

        token = create_access_token(
            user
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )