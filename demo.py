
from fusyona.utils.image import GetImageFromStorage
from fusyona.nft import PostCreateCollection

bearerToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJleHAiOjE2NjI4NjA0NzIsIm5iZiI6MTY2Mjg1Njg3MiwidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5mdXN5b25hLmNvbS9mOTE0MTYyZC1jMGMzLTQ5MGItOTNkNS0xZDhjZmUxYTQ3OTkvdjIuMC8iLCJzdWIiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJhdWQiOiI4N2FiZWQ5NC0yNWY0LTRmMmMtOWNmMi1kMjk4ODMyODlkM2EiLCJub25jZSI6IjkxMTM0OGQwLWI3OWEtZjMwNS1lMjcxLWJiNWY2ZmUxZTFiYiIsImlhdCI6MTY2Mjg1Njg3MiwiYXV0aF90aW1lIjoxNjYyODU2ODcyLCJvaWQiOiJmYWVmMjIzZi0zZjM4LTRkYTAtYTc3Zi1iODZjOTA2MjUyZTAiLCJnaXZlbl9uYW1lIjoiTGVhbmRybyIsImZhbWlseV9uYW1lIjoibGxscmRneiIsImVtYWlscyI6WyJsZWFuZHJvX19yb2RyaWd1ZXpAb3V0bG9vay5jb20iXSwidGZwIjoiQjJDXzFfU2lnblVwSW4ifQ.EKmMYvunwzLg5jLe4oa93mEbsJ9ZlQ1o61Djq0hV13bItKZZtPz1zbDvEIxPdYWEkxQVFi8F_dxIWxGigS0zs3a09azwJA7PJaq65vvHgT1zg0eLuTMRjjog7dJeT1adKHfREnCfKGFVi2PWU2DYNRkxCSRZNH9j9pAesWzCM5z5xJgyTdiVZ6v2ssrwzVZ0e5qpZJx7933upVklgRbvVp6mPXdADeIBDDwIkg0K4rFg4lRTbL84ETjgBIUTIuq0ECgzWmoo0SsDZp6wq9xgneM9Qth-8UXv8PpBfhSoVVuH_dKmz1RiaX7F7y3oVKxS3fXqjwzMFTJIEF09XRfTtA"

subscriptionKey="710e277524cc426baf6c8ef1eb930af5;product=starter"

blockchainNetwork = "Polygon"
name = "Wallpaper 5.2"
description = "A collection of wallpapers 5.0 without problems 🤟" 
royalties = 78.1
category = "Art"
externalLink = "www.fusyona.com"
coverImage = GetImageFromStorage("/home/leandro/pictures/wallpaper2.jpg")
logoImage = GetImageFromStorage("/home/leandro/pictures/wallpaper2.jpg")
featuredImage = GetImageFromStorage("/home/leandro/pictures/wallpaper2.jpg")

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
