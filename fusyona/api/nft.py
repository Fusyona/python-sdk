
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

