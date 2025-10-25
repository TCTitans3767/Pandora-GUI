import json
from pydantic import BaseModel

class StartingSize(BaseModel):
    width: int
    height: int

class Settings(BaseModel):
    def __init__(self, file_path: str):
        with open(file_path, 'r') as f:
            data = json.load(f)
        super().__init__(**data)

    app_name: str
    starting_size: StartingSize