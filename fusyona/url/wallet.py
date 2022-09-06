

from typing import Callable


BalanceAsync : Callable [[str], str] = lambda address_id : f"https://api.fusyona.com/wallet/v1/addresses/{address_id}/balance" 
"""GET : BalanceAsync"""

FullBalanceAsync : Callable [[str], str] = lambda address_id : f"https://api.fusyona.com/wallet/v1/addresses/{address_id}/fullbalance" 
"""GET : FullBalanceAsync"""

ClientAddressesAndBalanceAsync : Callable [[], str] = lambda : f"https://api.fusyona.com/wallet/v1/fulladdresses" 
"""GET : GetClientAddressesAndBalanceAsync"""

CryptocurrenciesAsync : Callable [[], str] = lambda : f"https://api.fusyona.com/wallet/v1/cryptocurrencies" 
"""GET : CryptocurrenciesAsync"""

CryptocurrencySubUnistAsync: Callable [[str], str] = lambda cryptocurrency_id : f"https://api.fusyona.com/wallet/v1/cryptocurrencies/{cryptocurrency_id}/subunits" 
"""GET : CryptocurrencySubUnistAsync"""

WithdrawalAsync :  Callable [[str, str, str], str] = lambda address_id, to_public_key, amount :  f"https://api.fusyona.com/wallet/v1/addresses/{address_id}/transfer/{to_public_key}/{amount}" 
"""POST: WithdrawalAsync"""

