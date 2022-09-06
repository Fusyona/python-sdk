

from typing import Any
import fusyona.constants.url as url
from fusyona.api.utils.common import ConstructRequest


def PostCheckout(
        bearerToken : str, subscriptionKey : str 
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.Checkout,
        params=[]
    )


def PostCheckoutCancel(
        bearerToken : str, subscriptionKey : str, 
        id : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CheckoutCancel,
        params=[id]
    )


def PostCheckoutConfirmation(
        bearerToken : str, subscriptionKey : str,
        id : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CheckoutConfirmation,
        params=[id]
    )


def PostClaimGift(
        bearerToken : str, subscriptionKey : str,
        tokenId : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.ClaimGift,
        params=[tokenId]
    )


def GetInvoices(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.Invoices,
        params=[]
    )


def GetOrders(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.Orders,
        params=[]
    )

