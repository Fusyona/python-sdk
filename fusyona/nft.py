
import requests
from typing import Any
import fusyona.url.nft as url
from fusyona.utils.common import GetHeaders, ConstructRequest


def GetCollectionWithPagination(
        bearerToken : str, subscriptionKey : str, 
        pageNumber : int
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CollectionsWithPagination,
        params=[pageNumber]
    )


def GetCollectionsList(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CollectionsList,
        params=[]
    )


def PostCreateCollection(
        bearerToken : str, subscriptionKey : str,
        coverImage : bytes, logoImage : bytes,
        featuredImage : bytes, blockchainNetwork : str,
        name : str, description : str, 
        royalties : float, category : str,
        externalLink : str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    files = {
        "CoverImage": coverImage,  
        "LogoImage": logoImage, 
        "FeaturedImage": featuredImage
    }

    body = {
        "BlockchainNetwork": blockchainNetwork,
        "Name": name,
        "Description" : description, 
        "Royalties" : str(royalties),
        "Category" : category,
        "ExternalLink" : externalLink,
    }

    response = requests.post(
        url=url.CreateCollection(), headers=headers, 
        data=body, files=files
    )

    if response.status_code != 200:
        raise Exception("There is an error with the creation")

    approvedLink = response.json()['payment']['value']['approvedLink']

    if len(approvedLink) == 0:
        raise Exception(f"Error {response.status_code}: approvedLink is empty")

    response = requests.post(url=approvedLink, headers=headers)

    if len(response.content) != 0:
        return response

    return { "Response" : str(response.status_code)}


def GetSingleCollection(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.SingleCollection,
        params=[collectionId]
    )


def PostCreateToken(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CreateToken,
        params=[collectionId]
    )


def GetSingleToken(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str, tokenId : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.SingleToken,
        params=[collectionId, tokenId]
    )

  
def GetTokensList(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.TokensList,
        params=[collectionId]
    )


def GetTokensListWithPagination(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str, pageNumber : int
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.TokensListWithPagination,
        params=[collectionId, pageNumber]
    )


def GetGiftsListWithPagination(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str, pageNumber : int
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GiftsListWithPagination,
        params=[collectionId, pageNumber]
    )

    
def PostPaymentConfirmation(
        bearerToken : str, subscriptionKey : str, 
        id : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.PaymentConfirmation,
        params=[id]
    )


def PostPaymentCancel(
        bearerToken : str, subscriptionKey : str, 
        id : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.PaymentCancel,
        params=[id]
    )

