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

def create_task(
    title,
    description,
    current_user
):
    
    last_task = tasks_collection.find_one(
        sort=[("id", -1)]
    )

    new_id = (
        1
        if last_task is None
        else last_task["id"] + 1
    )

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "to do",
        "owner_id": current_user["id"]
    }

    tasks_collection.insert_one(
        new_task
    )

    print(new_task)
    return new_task

def get_all_tasks(
    current_user,
    q=None,
    status=None
):

    filters = {
        "owner_id": current_user["id"]
    }

    if status:
        filters["status"] = status.value

    tasks = list(
        tasks_collection.find(filters)
    )

    for task in tasks:
        task.pop("_id", None)

    if q:

        q = q.lower()

        tasks = [
            task
            for task in tasks
            if (
                q in task["title"].lower()
                or q in task["description"].lower()
            )
        ]

    return tasks

def get_task(
    task_id,
    current_user
):

    task = (
        tasks_collection.find_one(
            {
                "id": task_id,
                "owner_id":
                current_user["id"]
            }
        )
    )

    if task is None:
        raise ValueError(
            "Task not found"
        )

    task.pop("_id", None)
    return task

def update_task(
    task_id: int, 
    task_data: TaskUpdate,
    current_user
    ):

    task = get_task(
        task_id,
        current_user
        )

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
        {
            "id": task_id,
            "owner_id": current_user["id"]
        },
        {
            "$set": update_fields
        }
    )

    return get_task(
        task_id,
        current_user
    )

def delete_task(
    task_id,
    current_user
    ):

    task = get_task(
        task_id,
        current_user
    )
    
    tasks_collection.delete_one(
    {
        "id": task_id,
        "owner_id":
        current_user["id"]
    }
)

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