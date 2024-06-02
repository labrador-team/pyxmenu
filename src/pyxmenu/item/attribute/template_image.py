import base64

from pyxmenu.item.attribute.__base__ import Attribute, AttributeName, INVALID_ATTRIBUTE_VALUE


class TemplateImageAttribute(Attribute):
    """
    Controls the image that will be used as the template for the item.
    """

    _name_ = AttributeName.TEMPLATE_IMAGE

    def parse(self, value: str):
        try:
            base64.b64decode(value)
            return value
        except Exception:
            return INVALID_ATTRIBUTE_VALUE
