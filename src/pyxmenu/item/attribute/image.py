import base64

from pyxmenu.item.attribute.__base__ import Attribute, INVALID_ATTRIBUTE_VALUE


class ImageAttribute(Attribute):
    """
    Controls the image of an item.
    """

    def parse(self, value: str):
        try:
            base64.b64decode(value)
            return value
        except Exception:
            return INVALID_ATTRIBUTE_VALUE
