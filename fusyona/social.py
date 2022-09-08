from pickletools import int4, long1
from tkinter.tix import INTEGER
import fusyona.url.social as url
from fusyona.utils.common import ConstructRequest

def GetPages(
        bearerToken : str, subscriptionKey : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPages,
        params=[]
    )

def DeletePage(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePage,
        params=[page_id]
    )

def GetPage(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPage,
        params=[page_id]
    )

def PutPage(
        bearerToken : str, subscriptionKey : str,
        page_id : str,
        title: str,
        description: str,
        followers: int,
        profileImage: bytes,
        coverImage: bytes,
        decimals: int,
        name: str,
        symbol: str,
        totalSupply: int,
        address: str,
        web: str,
        phone: str,
        email: str,
        whatsapp: str,
        facebookURL: str,
        instagramURL: str,
        linkedInURL: str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    files = {
        "ProfileImage": profileImage,  
        "LogoImage": logoImage
    }

    body = {
        "title": title,
        "description": description,
        "followers": followers,
        "profileImage": profileImage,
        "coverImage": coverImage,
        "decimals": decimals,
        "name": name,
        "symbol": symbol,
        "totalSupply": totalSupply,
        "address": address,
        "web": web,
        "phone": phone,
        "email": email,
        "whatsapp": whatsapp,
        "facebookURL": facebookURL,
        "instagramURL": instagramURL,
        "linkedInURL": linkedInURL
    }

    response = requests.post(
        url=url.PutPage, headers=headers, 
        data=body, files=files
    )

    if response.status_code != 200:
        raise Exception("There is an error with the creation")

    approvedLink = response.json()['payment']['value']['approvedLink']

    if len(approvedLink) == 0:
        raise Exception(f"Error {response.status_code}: approvedLink is empty")

    response = requests.post(url=approvedLink, headers=headers)

    if len(response.content) != 0:
        return response.json()

    return { "Response" : str(response.status_code)}