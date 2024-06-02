from typing import Any

from pyxmenu.item.attribute.__base__ import Attribute, INVALID_ATTRIBUTE_VALUE


class TerminalAttribute(Attribute):
    """
    Controls whether the shell command should be shown in a terminal window or ran in the background.
    """

    def parse(self, value: Any):
        try:
            return bool(value)
        except ValueError:
            return INVALID_ATTRIBUTE_VALUE
