
from fusyona.utils.image import GetImageFromStorage
from fusyona.nft.nft import PostCreateCollection

bearerToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZ1c3lvbmEuY29tL2Y5MTQxNjJkLWMwYzMtNDkwYi05M2Q1LTFkOGNmZTFhNDc5OS92Mi4wLyIsImV4cCI6MTY2MzI3OTE5NywibmJmIjoxNjYzMjc1NTk3LCJhdWQiOiI4N2FiZWQ5NC0yNWY0LTRmMmMtOWNmMi1kMjk4ODMyODlkM2EiLCJvaWQiOiIxNThkOTE3Mi1kMWM1LTQwN2ItODU4ZS1lM2Q1MzhmNjFjZjciLCJzdWIiOiIxNThkOTE3Mi1kMWM1LTQwN2ItODU4ZS1lM2Q1MzhmNjFjZjciLCJnaXZlbl9uYW1lIjoiUm9sYW5kbyIsImZhbWlseV9uYW1lIjoiU2FuY2hleiBSYW1vcyIsImVtYWlscyI6WyJyb2xzYW5jaGV6QHlhbmRleC5jb20iXSwidGZwIjoiQjJDXzFfU2lnblVwSW4iLCJub25jZSI6ImQzNmI4YzY3LTY4NDMtNDI0ZS05ZWFmLTQ2YmMwZTkzMjA2MCIsInNjcCI6IldyaXRlVXNlclByb2ZpbGVBUEkgUmVhZFVzZXJQcm9maWxlQVBJIiwiYXpwIjoiZWI5MzY3MDctNTkzZS00OWQzLTgwMjgtMTA3NjBkNWI5YjI5IiwidmVyIjoiMS4wIiwiaWF0IjoxNjYzMjc1NTk3fQ.C7yJ2pKxHN_MtS1CiZVmXWtXNwAwphafux26epawL4cssXlgr0OjukKkJ7bccZDkbLVccpRdYODbA7PGYGc0P316cs3EPBlbUjIh_LnqjcBXvo9m5Xv5cYcahz9X-ZUkRKiOiMVADJfs6e0v4F1i1BYhC5VPArssJbk-uXNj2RoQnnPNlKjgrd7v13Ohk_F7Cs289JjraAh2SJWoNoR16xlOgC4hF4w2URfmcgO2kQNcfey3viPAgS_1GVmmx844pSfMZGzPQSTcxiUx64ptUfxntH3NPtZS9q9bIchEFnOd231brM9sm1VAL6ocfr6Y6iSiO646dqPLDOYeUSEwvw"

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

