

from typing import Callable


CreateCollection: Callable[[], str] = lambda : "https://nft-marketplace-api.azurewebsites.net/api/collections"
"""method: `POST`\ndescription: Get the link for creating an NFT collection"""

CreateToken: Callable[[str], str] = lambda collectionId : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}/tokens"
"""POST: CreateToken"""

CollectionsList: Callable[[], str] = lambda : "https://nft-marketplace-api.azurewebsites.net/api/collections"
"""GET: CollectionsList"""

CollectionsWithPagination: Callable[[int], str] = lambda pageNumber : f"https://nft-marketplace-api.azurewebsites.net/api/collections/pages/{str(pageNumber)}"
"""GET: CollectionsWithPagination"""

GiftsListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}/gifts/pages/{str(pageNumber)}"
"""GET: GiftsListWithPagination"""

SingleCollection: Callable[[str], str] = lambda collectionId : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}"
"""GET: SingleCollection"""

SingleToken: Callable[[str, str], str] = lambda collectionId, tokenId : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}/tokens/{tokenId}"
"""GET: SingleToken"""

TokensList: Callable[[str], str] = lambda collectionId : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}/tokens"
"""GET: TokensList"""

TokensListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : f"https://nft-marketplace-api.azurewebsites.net/api/collections/{collectionId}/tokens/pages/{pageNumber}"
"""GET: TokensListWithPagination"""

PaymentCancel: Callable[[str], str] = lambda id : f"https://nft-marketplace-api.azurewebsites.net/api/PaymentCancel/{id}"
"""POST: PaymentCancel"""

PaymentConfirmation: Callable[[str], str] = lambda id : f"https://nft-marketplace-api.azurewebsites.net/api/PaymentConfirmation/{id}"
"""POST: PaymentConfirmation"""

