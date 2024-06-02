from typing import Any

from pyxmenu.item.attribute.__base__ import Attribute, AttributeName, INVALID_ATTRIBUTE_VALUE


class AlternateAttribute(Attribute):
    """
    The alternate attribute x-bar uses.

    Notes:
        This attribute is fully managed by pyxmenu and should not be accessed directly.
    """

    def parse(self, value: Any):
        try:
            return bool(value)
        except ValueError:
            return INVALID_ATTRIBUTE_VALUE


class AlternativeAttribute(Attribute):
    """
    Controls whether to interpret the next item as an alternative item or not.
    """

    def parse(self, value: Any):
        from pyxmenu.item import Item

        if not isinstance(value, Item):
            return INVALID_ATTRIBUTE_VALUE

        return value

    def __str__(self):
        if self.value == INVALID_ATTRIBUTE_VALUE:
            return INVALID_ATTRIBUTE_VALUE

        self.value.attributes[AttributeName.ALTERNATE] = AlternateAttribute(True)
        return f'\n{self.value}'
