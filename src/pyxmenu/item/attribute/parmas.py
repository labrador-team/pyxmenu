from typing import Any

from pyxmenu.item.attribute.__base__ import Attribute, INVALID_ATTRIBUTE_VALUE


class ParamsAttribute(Attribute):
    """
    Controls the params of the item that will be passed to the shell command.

    This ties in to the `param1` described in the
    [xbar documentation](https://github.com/matryer/xbar-plugins/blob/main/CONTRIBUTING.md#parameters)
    """

    def parse(self, value: Any):
        if isinstance(value, str):
            return [item.strip() for item in value.split(",")]

        if isinstance(value, list):
            return [str(item) for item in value]

        return INVALID_ATTRIBUTE_VALUE

    def __str__(self):
        return ' '.join([f'param{index + 1}="{value}"' for index, value in enumerate(self.value)])
