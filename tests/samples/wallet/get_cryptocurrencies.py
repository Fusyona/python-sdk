
from fusyona.wallet.wallet import GetCryptocurrenciesAsync

addressId="4fc3baf2-8284-4979-b0f0-7d01cbef1dee"
bearerToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJleHAiOjE2NjQwNDE0ODcsIm5iZiI6MTY2NDAzNzg4NywidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5mdXN5b25hLmNvbS9mOTE0MTYyZC1jMGMzLTQ5MGItOTNkNS0xZDhjZmUxYTQ3OTkvdjIuMC8iLCJzdWIiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJhdWQiOiI4N2FiZWQ5NC0yNWY0LTRmMmMtOWNmMi1kMjk4ODMyODlkM2EiLCJub25jZSI6IjRkNjQxZDNiLWRiNmUtZTZmMC02Mzk1LTI0NmE0YWQ5NmE1OSIsImlhdCI6MTY2NDAzNzg4NywiYXV0aF90aW1lIjoxNjY0MDM3ODg3LCJvaWQiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJnaXZlbl9uYW1lIjoiTGVhbmRybyIsImZhbWlseV9uYW1lIjoibGxscmRneiIsImVtYWlscyI6WyJsZWFuZHJvX19yb2RyaWd1ZXpAb3V0bG9vay5jb20iXSwidGZwIjoiQjJDXzFfU2lnblVwSW4ifQ.fg-cXoL83PpNl7YmCGpRwCSUFh0_j8XvxrhCSu8Z8-tUykRn2dI-ODfk-i8ldBxxA6f3NAjJX4quPSPT1jpHiuQIlxEr5BVUMU-SKfYQZpM1bBuKJxhiX5vDa1_SkuPqskuv2DttUhLe8yDZb379hW20Xv-ww_BRJ56CmFQOfZiycZwfFcQqLojVJaXULvtmzLNDNCPjXDkJTBEqnWBRfXM-9-CnbhkVo9_JnF6tNVzmyrLdTrJ_tyO-qtHRJLoA2zCGboYt2d3ytH0vxsnAq_MKTedKTTvSoWbeuVXTpG59x2MlxPDM4pNjJZfxPEM2joy1Ijha-Gb3GvI7XsA59Q"
subscriptionKey="710e277524cc426baf6c8ef1eb930af5;product=starter"

respons = GetCryptocurrenciesAsync(
    bearerToken=bearerToken,
    subscriptionKey=subscriptionKey
)

print(GetCryptocurrenciesAsync)
