

from typing import Any
import fusyona.user.url as url
from fusyona.utils.common import ConstructRequest


def GetUserProfile(
        bearerToken : str, subscriptionKey : str, 
        user_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.UserProfile,
        params=[user_id]
    )


