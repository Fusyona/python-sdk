
from requests.structures import CaseInsensitiveDict

def GetHeaders(bearerToken, subscriptionKey) -> CaseInsensitiveDict:
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {bearerToken}"
    headers["Ocp-Apim-Trace"] = "true"
    headers["Ocp-Apim-Subscription-Key"] = subscriptionKey
    
    return headers
