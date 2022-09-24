
from pydantic import BaseModel
from fusyona.wallet.models.cryptocurrency import Cryptocurrency

class Balance(BaseModel):
    available: str | None
    in_orders: str | None
    cryptocurrency: Cryptocurrency | None
