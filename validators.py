VALID_STATUS = ["to do", "in progress", "completed"]

def validate_status(status):
    if status is None:
        return

    value = status.value if hasattr(status, "value") else status

    if value not in VALID_STATUS:
        raise ValueError("Invalid status")  

def validate_title(title: str):
    if not title.strip():
        raise ValueError("Title cannot be empty")

def validate_description(description: str):
    if not description.strip():
        raise ValueError("Description cannot be empty")