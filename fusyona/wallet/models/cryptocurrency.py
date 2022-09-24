
from pydantic import BaseModel

class Cryptocurrency(BaseModel):
    id: str | None
    label: str | None
    symbol: str | None
    decimals: str | None
    profileURL: str | None
    depositFee: str | None
    withdrawalFee: str | None
