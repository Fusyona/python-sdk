
from pydantic import BaseModel
from fusyona.wallet.models.cryptocurrency import Cryptocurrency
from fusyona.wallet.models.balance import Balance
from fusyona.wallet.models.currency_fee import Currency_Fee

class Client_Address(BaseModel):
    id: str | None
    cryptocurrency: Cryptocurrency | None
    currency_fee: Currency_Fee | None
    balance: Balance | None
    label: str | None
    public_key: str | None
    status: str | None
