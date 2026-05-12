from validators import (
    validate_status,
    validate_title,
    validate_description
)

TASK_LIST = {}

def create_task(title: str, description: str):
    validate_title(title)
    validate_description(description)

    new_id = max(TASK_LIST.keys(), default=0) + 1 #Nova lógica: calcular o novo id para evitar variável global

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": 'to do' #Já inicializa a nova tarefa com o status "to do"
    }
   
    TASK_LIST[new_id] = new_task
    return new_task #Retorna a task alocada em TASK_LIST[]

def get_all_tasks():
    return list(TASK_LIST.values())

def get_task(task_id: int):
    task = TASK_LIST.get(task_id)

    if task is None:
        raise ValueError("Task not found")

    return task

def update_task(task_id: int, new_status: str):
    task = get_task(task_id) #verifica a existência da task
    validate_status(new_status) #verifica validade do status
    
    task["status"] = new_status
    return task

def delete_task(task_id):
   task = get_task(task_id)
   del TASK_LIST[task_id]
   return task