
from typing import Callable

# ======================================
# ================ NFTs ================
# ======================================

CreateCollection: Callable[[], str] = lambda : "https://api.fusyona.com/nfts/v1/collections"
"""method: `POST`\ndescription: Get the link for creating an NFT collection"""

CreateToken: Callable[[str], str] = lambda collectionId : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}/tokens"
"""POST: CreateToken"""

CollectionsList: Callable[[], str] = lambda : "https://api.fusyona.com/nfts/v1/collections"
"""GET: CollectionsList"""

CollectionsWithPagination: Callable[[int], str] = lambda pageNumber : f"https://api.fusyona.com/nfts/v1/collections/pages/{str(pageNumber)}"
"""GET: CollectionsWithPagination"""

GiftsListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}/gifts/pages/{str(pageNumber)}"
"""GET: GiftsListWithPagination"""

SingleCollection: Callable[[str], str] = lambda collectionId : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}"
"""GET: SingleCollection"""

SingleToken: Callable[[str, str], str] = lambda collectionId, tokenId : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}/tokens/{tokenId}"
"""GET: SingleToken"""

TokensList: Callable[[str], str] = lambda collectionId : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}/tokens"
"""GET: TokensList"""

TokensListWithPagination: Callable[[str, int], str] = lambda collectionId, pageNumber : f"https://api.fusyona.com/nfts/v1/collections/{collectionId}/tokens/pages/{pageNumber}"
"""GET: TokensListWithPagination"""

PaymentCancel: Callable[[str], str] = lambda id : f"https://api.fusyona.com/nfts/v1/PaymentCancel/{id}"
"""POST: PaymentCancel"""

PaymentConfirmation: Callable[[str], str] = lambda id : f"https://api.fusyona.com/nfts/v1/PaymentConfirmation/{id}"
"""POST: PaymentConfirmation"""

#########################################
################ Wallet #################  
#########################################  

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

#########################################
################ Payment ################  
#########################################  

Checkout :  Callable [[str, str, str], str] = lambda address_id, to_public_key, amount :  f"https://api.fusyona.com/pay/v1/Checkout" 
"""POST: Checkout"""

CheckoutCancel :  Callable [[str], str] = lambda id :  f"https://api.fusyona.com/pay/v1/CheckoutCancel/{id}" 
"""POST: CheckoutCancel"""

CheckoutConfirmation :  Callable [[str], str] = lambda id :  f"https://api.fusyona.com/pay/v1/CheckoutConfirmation/{id}" 
"""POST: CheckoutConfirmation"""

ClaimGift :  Callable [[str], str] = lambda tokenId :  f"https://api.fusyona.com/pay/v1/{tokenId}/claim" 
"""POST: ClaimGift"""

Invoices : Callable [[], str] = lambda : f"https://api.fusyona.com/pay/v1/Invoices" 
"""GET : Invoices"""

Orders : Callable [[], str] = lambda : f"https://api.fusyona.com/pay/v1/Orders" 
"""GET : Orders"""

#########################################
############ Utility Tokens #############  
#########################################

CreateERC20 :  Callable [[], str] = lambda :  f"https://api.fusyona.com/utility/v1/erc20" 
"""POST: CreateERC20"""



#########################################
################ Social #################  
#########################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#