
from typing import Callable

# ======================================
# ================ NFTs ================
# ======================================

CreateCollection: Callable[[], str] = lambda : "https://api.fusyona.com/nfts/v1/collections"
"""method: `POST`\ndescription: Get the link for creating an NFT collection"""

CreateToken: Callable[[str], str] = lambda collectionId : "https://api.fusyona.com/nfts/v1/collections/" + collectionId +"/tokens"
"""POST: CreateToken"""

CollectionsList: Callable[[], str] = lambda : "https://api.fusyona.com/nfts/v1/collections"
"""GET: CollectionsList"""

CollectionsWithPagination: Callable[[int], str] = lambda pageNumber : "https://api.fusyona.com/nfts/v1/collections/pages/" + str(pageNumber)
"""GET: CollectionsWithPagination"""

GiftsListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : "https://api.fusyona.com/nfts/v1/collections/" + collectionId + "/gifts/pages/" + str(pageNumber)
"""GET: GiftsListWithPagination"""

SingleCollection: Callable[[str], str] = lambda collectionId : "https://api.fusyona.com/nfts/v1/collections/" + collectionId
"""GET: SingleCollection"""

SingleToken: Callable[[str, str], str] = lambda collectionId, tokenId : "https://api.fusyona.com/nfts/v1/collections/" + collectionId + "/tokens/" + tokenId
"""GET: SingleToken"""

TokensList: Callable[[str], str] = lambda collectionId : "https://api.fusyona.com/nfts/v1/collections/" + collectionId + "/tokens"
"""GET: TokensList"""

TokensListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : "https://api.fusyona.com/nfts/v1/collections/" + collectionId + "/tokens/pages/" + pageNumber
"""GET: TokensListWithPagination"""

PaymentCancel: Callable[[str], str] = lambda id : "https://api.fusyona.com/nfts/v1/PaymentCancel/" + id
"""POST: PaymentCancel"""

PaymentConfirmation: Callable[[str], str] = lambda id : "https://api.fusyona.com/nfts/v1/PaymentConfirmation/" + id
"""POST: PaymentConfirmation"""
