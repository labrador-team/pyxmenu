import typing

from pyargos.argos_object import ArgosObject
from pyargos.consts import _ARGOS_SEPERATOR_STR, _NEW_LINE
from pyargos.item import ArgosItem


class ArgosSection(ArgosObject):
    """
    A section of items in argos.

    Attributes:
        name: The name of the section.
        items: The items in the section.
        text_size: The text size of the title of the section.
    """

    name: str
    items: typing.Iterable[ArgosItem]
    text_size: int

    def __init__(self, name: str, items: typing.Iterable[ArgosItem], text_size: int = 7):
        """
        Initiates an argos section containing the item specified.

        Args:
            name: The name of the section.
            items: The item in the section.
            text_size: The text size of the title of the section.
        """
        self.name = name
        self.items = items
        self.text_size = text_size

    def __str__(self):
        parts = [_ARGOS_SEPERATOR_STR, f'{self.name} | size={self.text_size}']
        parts += [str(item) for item in self.items]
        parts.append(_ARGOS_SEPERATOR_STR)

        return _NEW_LINE.join(parts)
