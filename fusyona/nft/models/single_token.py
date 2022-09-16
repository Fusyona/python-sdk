
from fusyona.nft.models.token import Token
from fusyona.nft.models.collection import Collection
from pydantic import BaseModel
from typing import List

class SingleToken(BaseModel):
    token: Token | None
    collection: Collection | None
    attributes: List | None
