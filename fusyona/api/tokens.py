

from typing import Any
import fusyona.constants.url as url
from fusyona.api.utils.common import ConstructRequest


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

