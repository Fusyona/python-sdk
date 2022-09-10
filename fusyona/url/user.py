
from typing import Callable

UserProfile: Callable[[str], str] = lambda user_id : f"http://bktuserprofileapi.azurewebsites.net/users/{user_id}"
"""method: `GET`\ndescription: Get user profile"""
