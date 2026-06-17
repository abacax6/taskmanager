from database import tasks_collection, users_collection
from auth import hash_password
from validators import (
    validate_status,
    validate_title,
    validate_description
)
from schemas import ( 
    TaskUpdate, 
    TaskStatus, 
    TaskCreate, 
    TaskResponse
)

def create_task(title: str, description: str):

    validate_title(title)
    validate_description(description)

    last_task = tasks_collection.find_one(
        sort=[("id", -1)]
    )

    new_id = 1 if last_task is None else last_task["id"] + 1

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "to do"
    }

    tasks_collection.insert_one(new_task)

def get_all_tasks(q: str | None = None, status: TaskStatus | None = None):

    tasks = list(tasks_collection.find())

    for task in tasks:
        task.pop("_id", None)

    # filtros continuam iguais...

    #filtro por texto
    if q:
        q = q.lower()

        tasks = [
            task for task in tasks
            if q in task["title"].lower()
            or q in task["description"].lower()
        ]

    #filtro status
    if status:
        tasks = [
            task for task in tasks
            if task["status"] == status.value
        ]
    return tasks

def get_task(task_id: int):

    task = tasks_collection.find_one({"id": task_id})

    if task is None:
        raise ValueError("Task not found")

    task.pop("_id", None)

    return task

def update_task(task_id: int, task_data: TaskUpdate):

    task = get_task(task_id)

    update_fields = {}

    if task_data.title is not None:
        validate_title(task_data.title)
        update_fields["title"] = task_data.title

    if task_data.description is not None:
        validate_description(task_data.description)
        update_fields["description"] = task_data.description
    
    if task_data.status is not None:
        validate_status(task_data.status)
        update_fields["status"] = task_data.status.value

    tasks_collection.update_one(
        {"id": task_id},
        {"$set": update_fields}
    )

    return get_task(task_id)

def delete_task(task_id: int):

    task = get_task(task_id)

    tasks_collection.delete_one({"id": task_id})

    return task

def create_user(email, password):

    existing = users_collection.find_one(
        {"email": email}
    )

    if existing:
        raise ValueError(
            "Email already registered"
        )

    last_user = users_collection.find_one(
        sort=[("id",-1)]
    )

    new_id = (
        1
        if last_user is None
        else last_user["id"] + 1
    )

    user = {
        "id": new_id,
        "email": email,
        "password": hash_password(password)
    }

    users_collection.insert_one(
        user
    )

    return {
        "id": new_id,
        "email": email
    }