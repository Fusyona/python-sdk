
import json
import fusyona.constants.url as url
import requests
from fusyona.api.common import GetHeaders


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
