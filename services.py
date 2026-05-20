from validators import (
    validate_status,
    validate_title,
    validate_description
)

from schemas import TaskUpdate

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

def get_all_tasks():
    return list(TASK_LIST.values())

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