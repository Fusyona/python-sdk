
from fusyona.nft.models.attachment import Attachment
from datetime import datetime
from pydantic import BaseModel

class Collection(BaseModel):
    id: str | None
    author: str | None
    authorId: str | None
    type: str | None
    creactionDate: datetime | None
    category: str | None
    collectionId: str | None
    tags: str | None 
    privacy: str | None
    ownerId: str | None
    coverImage: Attachment | None
    logoImage: Attachment | None
    featuredImage: Attachment | None
    blockchainNetwork: str | None
    contractAddress: str | None
    externalLink: str | None
    name: str | None
    description: str | None
    royalties: str | None
    numberOfTokens: int | None
    status: str | None
    transactionHash: str | None

