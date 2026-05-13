VALID_STATUS = ["to do", "in progress", "completed"]

def validate_status(status: str):
    if status not in VALID_STATUS:
        #raise ValueError("Invalid status")  
        raise HTTPException(status_code=400, detail="Invalid status")  

def validate_title(title: str):
    if not title.strip(): #Verificação para título vazio.
        raise ValueError("Title cannot be empty")

def validate_description(description: str):
    if not description.strip():
        raise ValueError("Description cannot be empty")