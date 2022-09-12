from pickletools import int4, long1
from tkinter.tix import INTEGER
from unittest.mock import sentinel
from typing import Any

import requests
import fusyona.social.url as url
from fusyona.utils.common import ConstructRequest, GetHeaders

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
        "profileImage": profileImage,  
        "coverImage": coverImage
    }

    body = {
        "pageId": page_id,
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

    response = requests.put(
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

def PostPageFollow(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.PostPageFollow,
        params=[page_id]
    )

def GetPageFollowers(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPageFollowers,
        params=[page_id]
    )

def DeletePageFollower(
        bearerToken : str, subscriptionKey : str,
        page_id : str, follower_id : str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePageFollower,
        params=[page_id, follower_id]
    )

def GetPagePosts(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePosts,
        params=[page_id]
    )

def PostPagePost(
        bearerToken : str, subscriptionKey : str,
        page_id : str, category: str, privacy: str,
        content: str, attachment: list(str)
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "category": category,
        "privacy": privacy,
        "content" : content, 
        "attachment" : attachment,
    }

    response = requests.post(
        url=url.PostPagePost, headers=headers, 
        data=body
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

def DeletePagePost(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePagePost,
        params=[page_id, post_id]
    )

def GetPagePost(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePost,
        params=[page_id, post_id]
    )

def PutPagePost(
        bearerToken : str, subscriptionKey : str,
        page_id : str, oldAttachmentPaths: list(str),
        content: str, attachment: list(str)
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "content" : content, 
        "attachments" : attachment,
        "oldAttachmentPaths": oldAttachmentPaths
    }

    response = requests.put(
        url=url.PutPagePost, headers=headers, 
        data=body
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

def GetPagePostComments(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePostComments,
        params=[page_id, post_id]
    )

def PostPagePostComment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id: str,
        content: str, path: str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "postId": post_id,
        "content" : content, 
        "path" : path,
    }

    response = requests.post(
        url=url.PostPagePostComment, headers=headers, 
        data=body
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

def DeletePagePostComment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, comment_id: str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePagePostComment,
        params=[page_id, post_id, comment_id]
    )

def GetPagePostComment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, comment_id: str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePostComment,
        params=[page_id, post_id, comment_id]
    )

def PutPagePostComment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id: str,
        content: str, path: str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "postId": post_id,
        "content" : content, 
        "path" : path,
    }

    response = requests.put(
        url=url.PutPagePostComment, headers=headers, 
        data=body
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

def GetPagePostSentiments(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePostSentiments,
        params=[page_id, post_id]
    )

def PostPagePostSentiment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id: str,
        value: str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "postId": post_id,
        "value": value
    }

    response = requests.post(
        url=url.PostPagePostSentiment, headers=headers, 
        data=body
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

def DeletePagePostSentiment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, sentiment_id: str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePagePostSentiment,
        params=[page_id, post_id, sentiment_id]
    )

def GetPagePostSentiment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, sentiment_id: str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePostSentiment,
        params=[page_id, post_id, sentiment_id]
    )

def PutPagePostSentiment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id: str,
        value: str
    ) -> Any:

    headers = GetHeaders(
        bearerToken, 
        subscriptionKey
    )

    body = {
        "pageId": page_id,
        "postId": post_id,
        "value": value
    }

    response = requests.put(
        url=url.PutPagePostSentiment, headers=headers, 
        data=body
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

def DeletePagePostSentiment(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, sentiment_id: str
    ) -> Any:

    return ConstructRequest(
        method="delete", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.DeletePagePostSentiment,
        params=[page_id, post_id, sentiment_id]
    )

def GetPagePostWithPagination(
        bearerToken : str, subscriptionKey : str,
        page_id : str, post_id : str, pagination: str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagePostWithPagination,
        params=[page_id, post_id, pagination]
    )

def GetPageTokens(
        bearerToken : str, subscriptionKey : str,
        page_id : str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPageTokens,
        params=[page_id]
    )

def GetPageToken(
        bearerToken : str, subscriptionKey : str,
        page_id : str, token_id: str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPageToken,
        params=[page_id, token_id]
    )

def PostPageUnfollow(
        bearerToken : str, subscriptionKey : str, 
        collectionId : str, follower_id: str
    ) -> Any:

    return ConstructRequest(
        method="post", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.PostPageUnfollow,
        params=[collectionId, follower_id]
    )

def GetPagesWithPagination(
        bearerToken : str, subscriptionKey : str,
        page_id : str, pagination: str
    ) -> Any:

    return ConstructRequest(
        method="get", 
        bearerToken=bearerToken,
        subscriptionKey=subscriptionKey,
        getUrl=url.GetPagesWithPagination,
        params=[page_id,pagination]
    )