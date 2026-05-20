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

TASK_LIST = {}
NEXT_ID = 1

def create_task(title: str, description: str):
    global NEXT_ID

    validate_title(title)
    validate_description(description)

    new_task = {
        "id": NEXT_ID,
        "title": title,
        "description": description,
        "status": 'to do' #Já inicializa a nova tarefa com o status "to do"
    }
   
    TASK_LIST[NEXT_ID] = new_task
    NEXT_ID += 1 
    
    return new_task #Retorna a task alocada em TASK_LIST[]

def get_all_tasks(q: str | None = None, status: TaskStatus | None = None):
    tasks = list(TASK_LIST.values())

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
    task = TASK_LIST.get(task_id)

    if task is None:
        raise ValueError("Task not found")
        #raise HTTTPException(status_code=404, detail = "Task not found")

    return task

def update_task(task_id: int, task_data: TaskUpdate):
    task = get_task(task_id) #verifica a existência da task
    validate_title((task_data.title))
    validate_description(task_data.description)
    validate_status(task_data.status) #verifica validade do status
    
    task["title"] = task_data.title
    task["description"] = task_data.description
    if task_data.status is not None:
        task["status"] = task_data.status.value

    return task

def delete_task(task_id):
   task = get_task(task_id)
   del TASK_LIST[task_id]
   return task