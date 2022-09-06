

from typing import Any
import fusyona.url.token as url
from fusyona.utils.common import ConstructRequest


def PostCreateERC20(
        bearerToken : str, subscriptionKey : str 
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CreateERC20,
        params=[]
    )

