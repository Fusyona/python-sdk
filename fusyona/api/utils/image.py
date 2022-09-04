
# from os import getcwd
import requests


def GetImageFromStorage(address : str) -> bytes:

    return open(address, "rb")


def GetImageFromUrl(url : str) -> bytes:

    img_data = requests.get(url).content

    # with open('image_name.jpg', 'wb') as handler:
    #     handler.write(img_data)

    # imagen = GetImagenFromStorage(f"{getcwd()}/image_name.jpg")

    return img_data
