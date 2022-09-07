from fusyona import url
from fusyona.utils.common import ConstructRequest

def GetPages(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CollectionsList,
        params=[]
    )