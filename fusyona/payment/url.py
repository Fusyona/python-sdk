

from typing import Callable


Checkout :  Callable [[str, str, str], str] = lambda :  f"https://api.fusyona.com/pay/v1/Checkout" 
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

