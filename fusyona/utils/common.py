
import requests
from typing import Any, Callable, List
from requests.structures import CaseInsensitiveDict

def GetHeaders(bearerToken, subscriptionKey) -> CaseInsensitiveDict:
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {bearerToken}"
    headers["Ocp-Apim-Trace"] = "true"
    headers["Ocp-Apim-Subscription-Key"] = subscriptionKey
    
    return headers


def ConstructRequest(
        method : str, 
        bearerToken : str, 
        subscriptionKey : str, 
        getUrl : Callable, 
        params : List[Any]
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    response = requests.request(
        method=method,
        url=getUrl(*params), 
        headers=headers
    )

    return response

