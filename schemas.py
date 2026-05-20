from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    to_do = "to do"
    in_progress = "in progress"
    completed = "completed"

class TaskCreate(BaseModel): #Modelo Base para criar task
    title: str
    description: str

class TaskResponse(BaseModel): #Modelo da resposta esperada
    id: int
    title: str
    description: str
    status: TaskStatus

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None


