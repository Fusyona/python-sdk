
import json
import fusyona.constants.url as url
import requests
from fusyona.api.utils.common import GetHeaders


def GetCollectionWithPagination(bearerToken : str, subscriptionKey : str, pageNumber : int) -> json:
    
    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(
        url=url.CollectionsWithPagination(pageNumber), 
        headers=headers
    )

    return response.json()


def GetCollectionsList(bearerToken : str, subscriptionKey : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(
        url=url.CollectionsList(), 
        headers=headers
    )    

    return response.json()


def PostCreateCollection(
        bearerToken : str, subscriptionKey : str,
        coverImage : bytes, logoImage : bytes,
        featuredImage : bytes, blockchainNetwork : str,
        name : str, description : str, 
        royalties : float, category : str,
        externalLink : str
    ) -> json:

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

    response = requests.post(url=url.CreateCollection(), headers=headers, data=body, files=files)

    if response.status_code != 200:
        raise Exception("There is an error with the creation")

    approvedLink = response.json()['payment']['value']['approvedLink']

    if len(approvedLink) == 0:
        raise Exception(f"Error {response.status_code}: approvedLink is empty")

    response = requests.post(url=approvedLink, headers=headers)

    if len(response.content) != 0:
        return response.json()

    return { "Response" : str(response.status_code)}


def GetSingleCollection(bearerToken : str, subscriptionKey : str, collectionId : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.SingleCollection(collectionId), headers=headers)

    return response.json()


def PostCreateToken(bearerToken : str, subscriptionKey : str, collectionId : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.CreateToken(collectionId), headers=headers)

    return response.json()
    

def GetSingleToken(bearerToken : str, subscriptionKey : str, collectionId : str, tokenId : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.SingleToken(collectionId, tokenId), headers=headers)

    return response.json()

   
def GetTokensList(bearerToken : str, subscriptionKey : str, collectionId : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.TokensList(collectionId), headers=headers)
    
    return response.json()


def GetTokensListWithPagination(bearerToken : str, subscriptionKey : str, collectionId : str, pageNumber : int) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.TokensListWithPagination(collectionId, pageNumber), headers=headers)
    
    return response.json()


def GetGiftsListWithPagination(bearerToken : str, subscriptionKey : str, collectionId : str, pageNumber : int) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.get(url=url.GiftsListWithPagination(collectionId, pageNumber), headers=headers)
    
    return response.json()

    
def PostPaymentConfirmation(bearerToken : str, subscriptionKey : str, id : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.post(url=url.PaymentConfirmation(id), headers=headers)
    
    return response.json()


def PostPaymentCancel(bearerToken : str, subscriptionKey : str, id : str) -> json:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.post(url=url.PaymentCancel(id), headers=headers)
    
    return response.json()

