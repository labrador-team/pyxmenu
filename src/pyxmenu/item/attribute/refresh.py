from typing import Any

from pyxmenu.item.attribute.__base__ import Attribute, INVALID_ATTRIBUTE_VALUE


class RefreshAttribute(Attribute):
    """
    Controls whether to refresh the plugin when the item is triggered.
    """

    def parse(self, value: Any):
        try:
            return bool(value)
        except ValueError:
            return INVALID_ATTRIBUTE_VALUE
