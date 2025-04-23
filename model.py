from pydantic import BaseModel

class FileMetadata(BaseModel):
    filename: str
    file_size: int
    file_type: str
