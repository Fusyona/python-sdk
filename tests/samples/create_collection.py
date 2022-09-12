
from fusyona.utils.image import GetImageFromStorage
from fusyona.nft.nft import PostCreateCollection

bearerToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJleHAiOjE2NjI4OTIyMDAsIm5iZiI6MTY2Mjg4ODYwMCwidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5mdXN5b25hLmNvbS9mOTE0MTYyZC1jMGMzLTQ5MGItOTNkNS0xZDhjZmUxYTQ3OTkvdjIuMC8iLCJzdWIiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJhdWQiOiI4N2FiZWQ5NC0yNWY0LTRmMmMtOWNmMi1kMjk4ODMyODlkM2EiLCJub25jZSI6IjNiZWUwZjRkLTBkNzYtZmEzMS00NDkzLTE4MzBhMGViYmJhMSIsImlhdCI6MTY2Mjg4ODYwMCwiYXV0aF90aW1lIjoxNjYyODg4NjAwLCJvaWQiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJnaXZlbl9uYW1lIjoiTGVhbmRybyIsImZhbWlseV9uYW1lIjoibGxscmRneiIsImVtYWlscyI6WyJsZWFuZHJvX19yb2RyaWd1ZXpAb3V0bG9vay5jb20iXSwidGZwIjoiQjJDXzFfU2lnblVwSW4ifQ.aT0BFcpq0QiHsTQjycYDMTUW1yJ-PLuTh_A6hZbb9nPi4SI5jZXG8TyezrxuEGkAEZKhxXNAXuRaQpNOK9j3qmTLhLti0WH_JW599q-HXVy2gwSpLMpp8H-S5s1PnueItzvw5BP4U0_JQhiPZsR2cISfTCBF1bpfjD0ukDtR-cUXTpwt9Gkf0nez-yfWuHXThDqho7DotQWJ3SZVDO5QdDODZMzmR1f_9osWrppucH45vEkG1CfSl54vFjitqox9A2NCVo-jzwplls9aai9NNWVlFnUcqnR2snuOZQj66WnUXz_R6ucuxmKBeZzIUVlIr4AsTn3lbW75HoczxIm_uQ"

subscriptionKey="710e277524cc426baf6c8ef1eb930af5;product=starter"

blockchainNetwork = "Polygon"
name = "Python SDK"
description = "A collection of samples created using the Python SDK"
royalties = 82.7
category = "Development"
externalLink = "www.fusyona.com"
coverImage = GetImageFromStorage("/home/leandro/pictures/python-sdk.png")
logoImage = GetImageFromStorage("/home/leandro/pictures/python-sdk.png")
featuredImage = GetImageFromStorage("/home/leandro/pictures/python-sdk.png")

print(
    PostCreateCollection(
        bearerToken=bearerToken, 
        subscriptionKey=subscriptionKey,
        coverImage=coverImage,
        logoImage=logoImage,
        featuredImage=featuredImage,
        blockchainNetwork=blockchainNetwork,
        name=name, description=description,
        royalties=royalties,
        category=category,
        externalLink=externalLink
    )
)
