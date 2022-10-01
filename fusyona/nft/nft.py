
import requests
from fusyona.nft.models.collection import Collection
from typing import Any, List
import fusyona.nft.url as url
from fusyona.utils.common import GetHeaders, ConstructRequest
from fusyona.nft.models.token import Token
from fusyona.nft.models.single_token import SingleToken


def GetCollectionWithPagination(
        bearerToken : str, 
        subscriptionKey : str, 
        pageNumber : int
    ) -> List[Collection]:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.CollectionsWithPagination(pageNumber)
    )

    return [Collection(**collection) for collection in response.json()['data']]


def GetCollectionsList(
        bearerToken : str, subscriptionKey : str
    ) -> List[Collection]:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.CollectionsList()
    )

    return [Collection(**collection) for collection in response.json()]


def PostCreateCollection(
        bearerToken : str, 
        subscriptionKey : str,
        coverImage : bytes, 
        logoImage : bytes,
        featuredImage : bytes, 
        blockchainNetwork : str,
        name : str, 
        description : str, 
        royalties : float, 
        category : str,
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
    ) -> Collection:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.SingleCollection(collectionId)
    )
    
    return Collection(**response.json())


def PostCreateToken(
        bearerToken : str, 
        subscriptionKey : str, 
        collectionId : str,
        attachment : bytes,
        title : str,
        description : str,
        category : str,
        supply : int,
        tags : str,
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    files = {
        "Attachment": attachment
    }

    body = {
        "Title": title,
        "Description" : description,
        "Category" : category,
        "Supply" : str(supply),
        "Tags" : tags,
        "Attributes" : "",
        "Privacy" : "Public",
        "ExternalLink" : "",
        "Codes" : "1234;3456;234234;",
    }

    response = requests.post(
        url=url.CreateToken(collectionId), headers=headers, 
        data=body, files=files
    )

    if response.status_code != 200:
        raise Exception(f"There is an error with the creation. Error: {response.status_code}")

    approvedLink = response.json()['payment']['value']['approvedLink']

    if len(approvedLink) == 0:
        raise Exception(f"Error {response.status_code}: approvedLink is empty")

    response = requests.post(url=approvedLink, headers=headers)

    if len(response.content) != 0:
        return response

    return { "Response" : str(response.status_code)}


def GetSingleToken(
        bearerToken : str, 
        subscriptionKey : str, 
        collectionId : str, 
        tokenId : str
    ) -> SingleToken:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.SingleToken(collectionId, tokenId)
    )

    return SingleToken(**response.json())

  
def GetTokensList(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str
    ) -> List[Token]:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.TokensList(collectionId)
    )
    print(response)
    return [Token(**token) for token in response.json()]


def GetTokensListWithPagination(
        bearerToken : str, 
        subscriptionKey : str, 
        collectionId : str, 
        pageNumber : int
    ) -> List[Token]:

    response = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.TokensListWithPagination(collectionId, pageNumber)
    )

    return [Token(**token) for token in response.json()['data']]

