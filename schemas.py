from pydantic import BaseModel

class TaskCreate(BaseModel): #Modelo Base para criar task
    title: str
    description: str

class TaskResponse(BaseModel): #Modelo da resposta esperada
    id: int
    title: str
    description: str
    status: str
