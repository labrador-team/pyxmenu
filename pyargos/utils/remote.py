import typing

import requests


def get_image_from_url(url: str, headers: typing.Optional[typing.Dict[str, typing.Any]] = None) \
        -> bytes:
    """
    Get the image data of an image url.

    Args:
        url: The url of the image.
        headers: The headers to get the image with.

    Returns:
        The image data.
    """
    return requests.get(url, headers=headers or {}).content
