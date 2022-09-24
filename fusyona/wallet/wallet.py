

from typing import Any
import fusyona.wallet.url as url
from fusyona.utils.common import ConstructRequest
from fusyona.wallet.models.balance import Balance
from fusyona.wallet.models.client_address import Client_Address
from fusyona.wallet.models.cryptocurrency import Cryptocurrency

def GetBalanceAsync(
        bearerToken : str, subscriptionKey : str, 
        address_id : str
    ) -> Balance:

    respons = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.BalanceAsync(address_id)
    )

    return Balance(**respons.json())


def GetFullBalanceAsync(
        bearerToken : str, subscriptionKey : str, 
        address_id : str
    ) -> Balance:

    respons = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.FullBalanceAsync(address_id)
    )

    return Balance(**respons.json())


def GetClientAddressesAndBalanceAsync(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    respons = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.ClientAddressesAndBalanceAsync()
    )

    return [Client_Address(**client) for client in respons.json()['list']]


def GetCryptocurrenciesAsync(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    respons = ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.CryptocurrenciesAsync()
    )

    return [Cryptocurrency(**crypto) for crypto in respons.json()['list']]


def GetCryptocurrencySubUnistAsync(
        bearerToken : str, subscriptionKey : str,
        cryptocurrency_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        url=url.CryptocurrencySubUnistAsync(cryptocurrency_id)
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
        url=url.WithdrawalAsync(address_id, to_public_key, amount)
    )

