

from typing import Callable

BASE_URL = "https://fusyona.azure-api.net/wallet/v1/"

BalanceAsync : Callable [[str], str] = lambda address_id : f"{BASE_URL}addresses/{address_id}/balance" 
"""GET : BalanceAsync"""

FullBalanceAsync : Callable [[str], str] = lambda address_id : f"{BASE_URL}addresses/{address_id}/fullbalance" 
"""GET : FullBalanceAsync"""

ClientAddressesAndBalanceAsync : Callable [[], str] = lambda : f"{BASE_URL}fulladdresses" 
"""GET : GetClientAddressesAndBalanceAsync"""

CryptocurrenciesAsync : Callable [[], str] = lambda : f"{BASE_URL}cryptocurrencies" 
"""GET : CryptocurrenciesAsync"""

CryptocurrencySubUnistAsync: Callable [[str], str] = lambda cryptocurrency_id : f"{BASE_URL}cryptocurrencies/{cryptocurrency_id}/subunits" 
"""GET : CryptocurrencySubUnistAsync"""

WithdrawalAsync :  Callable [[str, str, str], str] = lambda address_id, to_public_key, amount :  f"{BASE_URL}addresses/{address_id}/transfer/{to_public_key}/{amount}" 
"""POST: WithdrawalAsync"""

