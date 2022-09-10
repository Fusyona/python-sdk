from typing import Callable

GetPages: Callable[[], str] = lambda : f"https://api.fusyona.com/social/v1/pages"
"""method: `GET`\ndescription: Get pages"""

DeletePage: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}"
"""method: `DEL`\ndescription: Delete page"""

GetPage: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}"
"""method: `GET`\ndescription: Get page"""

PutPage: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}"
"""method: `PUT`\ndescription: Put page"""

PostPageFollow: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}/follow"
"""method: `POST`\ndescription: Post page follow"""

GetPageFollowers: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}/followers"
"""method: `GET`\ndescription: Get page followers"""

DeletePageFollower: Callable[[str, str], str] = lambda pageId, followerId : f"https://api.fusyona.com/social/v1/pages/{pageId}/followers/{followerId}"
"""method: `DEL`\ndescription: Delete page follower"""

GetPagePosts: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts"
"""method: `GET`\ndescription: Get page posts"""

PostPagePost: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts"
"""method: `POST`\ndescription: Post page post"""

DeletePagePost: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}"
"""method: `DEL`\ndescription: Delete page post"""

GetPagePost: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}"
"""method: `GET`\ndescription: Get page post"""

PutPagePost: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}"
"""method: `PUT`\ndescription: Put page post"""

GetPagePostComments: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/comments"
"""method: `GET`\ndescription: Get page post comments"""

PostPagePostComment: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/comments"
"""method: `POST`\ndescription: Post page post comment"""

DeletePagePostComment: Callable[[str, str, str], str] = lambda pageId, postId, commentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/comments/{commentId}"
"""method: `DEL`\ndescription: Delete page post comment"""

GetPagePostComment: Callable[[str, str, str], str] = lambda pageId, postId, commentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/comments/{commentId}"
"""method: `GET`\ndescription: Get page post comment"""

PutPagePostComment: Callable[[str, str, str], str] = lambda pageId, postId, commentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/comments/{commentId}"
"""method: `PUT`\ndescription: Put page post comment"""

GetPagePostSentiments: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/sentiments"
"""method: `GET`\ndescription: Get page post sentiments"""

PostPagePostSentiment: Callable[[str, str], str] = lambda pageId, postId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/sentiments"
"""method: `POST`\ndescription: Post page post sentiment"""

DeletePagePostSentiment: Callable[[str, str, str], str] = lambda pageId, postId, sentimentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/sentiments/{sentimentId}"
"""method: `DEL`\ndescription: Delete page post sentiment"""

GetPagePostSentiment: Callable[[str, str, str], str] = lambda pageId, postId, sentimentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/sentiments/{sentimentId}"
"""method: `GET`\ndescription: Get page post sentiment"""

PutPagePostSentiment: Callable[[str, str, str], str] = lambda pageId, postId, sentimentId : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/{postId}/sentiments/{sentimentId}"
"""method: `PUT`\ndescription: Put page post sentiment"""

GetPagePostWithPagination: Callable[[str, str], str] = lambda pageId, pageNumber : f"https://api.fusyona.com/social/v1/pages/{pageId}/posts/GetPage/{pageNumber}"
"""method: `GET`\ndescription: Get page post with pagination"""

GetPageTokens: Callable[[str], str] = lambda pageId : f"https://api.fusyona.com/social/v1/pages/{pageId}/tokens"
"""method: `GET`\ndescription: Get page tokens"""

GetPageToken: Callable[[str, str], str] = lambda pageId, tokenId : f"https://api.fusyona.com/social/v1/pages/{pageId}/tokens/{tokenId}"
"""method: `GET`\ndescription: Get page token"""

PostPageUnfollow: Callable[[str, str], str] = lambda pageId, followerId : f"https://api.fusyona.com/social/v1/pages/{pageId}/unFollow/{followerId}"
"""method: `POST`\ndescription: Post page unfollow"""

GetPagesWithPagination: Callable[[str, str], str] = lambda pageId, pageNumber : f"https://api.fusyona.com/social/v1/pages/page/{pageNumber}"
"""method: `GET`\ndescription: Get page with pagination"""