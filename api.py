from fastapi.security import (
    HTTPBearer
)
from fastapi import (
    FastAPI,
    Response,
    HTTPException,
    Depends
)
from schemas import ( 
    TaskUpdate, 
    TaskStatus, 
    TaskCreate, 
    TaskResponse,
    UserLogin,
    UserCreate,
    UserResponse,
    UserUpdate
)
from services import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task,
    create_user,
    update_user
)
from auth import (
    authenticate_user,
    create_access_token,
    get_current_user
)

app = FastAPI()

#Rotas
@app.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def list_tasks(

    q: str | None = None,
    status: TaskStatus | None = None,

    current_user=
    Depends(
        get_current_user
    )
):

    tasks = get_all_tasks(
        current_user,
        q,
        status
    )

    if not tasks:
        return Response(
            status_code=204
        )

    return tasks

@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def read_task(
    task_id: int,
    current_user=
    Depends(
        get_current_user
    )
):

    try:

        return get_task(
            task_id,
            current_user
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def add_task(
    task: TaskCreate,
    current_user=Depends(get_current_user)
):

    try:

        created = create_task(
            task.title,
            task.description,
            current_user
        )
    
        print(created)
        return created

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.patch(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def update(
    task_id: int,
    task_data: TaskUpdate,
    current_user=
    Depends(
        get_current_user
    )
):

    try:

        return update_task(
            task_id,
            task_data,
            current_user
        )

    except ValueError as e:

        message = str(e)

        if message == "Task not found":

            raise HTTPException(
                status_code=404,
                detail=message
            )

        raise HTTPException(
            status_code=400,
            detail=message
        )

@app.delete(
    "/tasks/{task_id}"
)
def remove_task(
    task_id: int,
    current_user=
    Depends(
        get_current_user
    )
):

    try:

        delete_task(
            task_id,
            current_user
        )

        return Response(
            status_code=204
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

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
def login(
    credentials: UserLogin
):

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

    except ValueError:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

@app.patch("/users/me")
def update_me(
    user_data: UserUpdate,
    current_user =
    Depends(get_current_user)
):

    update_user(
        current_user,
        user_data
    )

    return {
        "message":
        "Account updated. Please login again."
    }
