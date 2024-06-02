from typing import Any
from urllib.parse import urlparse

from pyxmenu.item.attribute.__base__ import Attribute, INVALID_ATTRIBUTE_VALUE


class HrefAttribute(Attribute):
    """
    Controls the URL that the item will open when triggered.
    """

    def parse(self, value: Any):
        value = str(value)

        try:
            result = urlparse(value)
            if all([result.scheme, result.netloc]):
                return value

            return INVALID_ATTRIBUTE_VALUE
        except AttributeError:
            return INVALID_ATTRIBUTE_VALUE
