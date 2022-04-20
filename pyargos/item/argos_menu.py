import os
import typing
from typing import Tuple

from pyargos.item.argos_item import ArgosItem
from pyargos.argos_object import ArgosObject


class ArgosMenu(ArgosObject):
    """
    Attributes:
        item: The item to represent the menu by.
        menu_items: The items of the menu.
    """

    item: ArgosItem
    menu_items = typing.Iterable[ArgosItem]

    def __init__(self, item: ArgosItem, menu_items: typing.Iterable[ArgosItem] = ()):
        """
        Initiates an argos menu item.
        The menu is represented with an item and holds inside multiple item.

        Args:
            item: The argos item to represent the menu as.
            menu_items: The item of the menu.
        """

        self.item = item
        self.menu_items = menu_items

    def __str__(self) -> str:
        string = str(self.item) + os.linesep

        string += \
            os.linesep.join(['--{}'.format(item_line)
                             for menu_item in self.menu_items
                             for item_line in str(menu_item).split(os.linesep)])

        return string
