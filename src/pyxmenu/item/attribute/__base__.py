import abc
from enum import Enum
from typing import Any

INVALID_ATTRIBUTE_VALUE = ''


class AttributeName(Enum):
    """
    Enum for the attribute names.
    """

    INVALID = None

    KEY = 'key'
    HREF = 'href'
    COLOR = 'color'
    FONT = 'font'
    SIZE = 'size'
    SHELL = 'shell'
    PARAMS = 'params'
    TERMINAL = 'terminal'
    REFRESH = 'refresh'
    DROPDOWN = 'dropdown'
    LENGTH = 'length'
    TRIM = 'trim'
    ALTERNATE = 'alternate'
    ALTERNATIVE = 'alternative'
    TEMPLATE_IMAGE = 'templateImage'
    IMAGE = 'image'
    EMOJIZE = 'emojize'
    ANSI = 'ansi'
    DISABLED = 'disabled'

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID


class Attribute(abc.ABC):
    _name_: AttributeName = NotImplemented
    value: Any = NotImplemented

    @classmethod
    @property
    def name(cls) -> AttributeName:
        """
        Get the attribute name.

        Notes:
            If the attribute name is not set, it will be set to the class name in lower case (if found in the
            AttributeName enum).

        Returns:
            The attribute name.
        """
        if cls._name_ is NotImplemented:
            cls._name_ = AttributeName(cls.__name__.replace("Attribute", "").lower())

        return cls._name_

    def __init__(self, value: Any):
        self.value = self.parse(value)

    def parse(self, value: Any) -> Any:
        """
        Parse the value.

        Notes:
            If the parse function returns `INVALID_ATTRIBUTE_VALUE` then the attribute will be ignored.

        Args:
            value: The value to parse.

        Returns:
            The parsed value.
        """
        return str(value)

    def __str__(self) -> str:
        """
        Get the string representation of the attribute.

        Returns:
            The string representation of the attribute.
        """
        if self.value is None:
            return INVALID_ATTRIBUTE_VALUE

        value = self.value
        if isinstance(self.value, bool):
            value = str(value).lower()

        return f'{self.name.value}="{value}"'
