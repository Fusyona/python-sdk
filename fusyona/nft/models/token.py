
from fusyona.nft.models.attachment import Attachment
from pydantic import BaseModel

class Token(BaseModel):
    id: str | None
    tokenId: str | None
    userId: str | None
    name: str | None
    description: str | None
    numberOfCopies: int | None
    jsonUrl: str | None
    attachmentUrl: str | None
    blockchainNetwork: str | None
    contractAddress: str | None
    creationDate: str | None
    author: str | None
    authorId: str | None
    authorEmail: str | None
    type: str | None
    status: str | None
    availableGifts: int | None
    totalOfGifts: int | None
    totalOfAuctions: int | None
    availableAuctions: int | None
    totalOfSells: int | None
    availableSells: int | None
    royalties: float | None
    transactionHash: str | None
    setURLTransactionHash: str | None
    setRoyaltiesTransactionHash: str | None
    collectionId: str | None
    currencyId: str | None
    attachment: Attachment | None
