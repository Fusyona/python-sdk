
from pydantic import BaseModel

class Attachment(BaseModel):
    id: str | None
    filePath: str | None
    contentType: str | None
