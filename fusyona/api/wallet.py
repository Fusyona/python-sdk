

from typing import Any
import fusyona.constants.url as url
from fusyona.api.utils.common import ConstructRequest


def GetBalanceAsync(
        bearerToken : str, subscriptionKey : str, 
        address_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.BalanceAsync,
        params=[address_id]
    )


def GetFullBalanceAsync(
        bearerToken : str, subscriptionKey : str, 
        address_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.FullBalanceAsync,
        params=[address_id]
    )


def GetClientAddressesAndBalanceAsync(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.ClientAddressesAndBalanceAsync,
        params=[]
    )


def GetCryptocurrenciesAsync(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CryptocurrenciesAsync,
        params=[]
    )


def GetCryptocurrencySubUnistAsync(
        bearerToken : str, subscriptionKey : str,
        cryptocurrency_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.CryptocurrencySubUnistAsync,
        params=[cryptocurrency_id]
    )


def GetWithdrawalAsync(
        bearerToken : str, subscriptionKey : str,
        address_id : str, to_public_key : str, 
        amount : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.WithdrawalAsync,
        params=[address_id, to_public_key, amount]
    )

