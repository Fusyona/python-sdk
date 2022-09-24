
from pydantic import BaseModel

class Currency_Fee(BaseModel):
    id: str | None
    label: str | None
    symbol: str | None
    profileURL: str | None
