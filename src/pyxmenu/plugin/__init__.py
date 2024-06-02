from typing import Optional, TypeVar

from pyxmenu import Item
from pyxmenu.section import Section


TPlugin = TypeVar('TPlugin', bound='Plugin')


class Plugin:
    """
    An x-bar plugin.

    Attributes:
        title: The title item of the plugin.
        items: The items of the plugin.
    """
    title: Item
    items: list[Item | Section]

    def __init__(self, title: Item, items: Optional[list[Item | Section]] = None):
        self.title = title
        self.items = items or []

    def add_item(self: TPlugin, item: Item | Section, index: Optional[int] = None) -> TPlugin:
        """
        Add an item to the plugin.

        Args:
            item: The item to add.
            index: The index to add the item at. If None, the item will be added at the end.

        Returns:
            The plugin itself.
        """
        if index is not None:
            self.items.insert(index, item)
        else:
            self.items.append(item)

        return self

    def add_items(self: TPlugin, items: list[Item | Section], index: Optional[int] = None) -> TPlugin:
        """
        Add multiple items to the plugin.

        Args:
            items: The items to add.
            index: The index to add the items at. If None, the items will be added at the end.

        Returns:
            The plugin itself.
        """
        if index is not None:
            self.items[index:index] = items
        else:
            self.items.extend(items)

        return self

    def remove_item(self: TPlugin, item: Item | Section) -> TPlugin:
        """
        Remove an item from the plugin.

        Args:
            item: The item to remove.

        Returns:
            The plugin itself.
        """
        self.items.remove(item)

        return self

    def remove_items(self: TPlugin, items: list[Item | Section]) -> TPlugin:
        """
        Remove multiple items from the plugin.

        Args:
            items: The items to remove.

        Returns:
            The plugin itself.
        """
        for item in items:
            self.items.remove(item)

        return self

    def pop_item(self: TPlugin, index: int) -> Item | Section:
        """
        Pop an item from the plugin.

        Args:
            index: The index of the item to pop.

        Returns:
            The popped item.
        """
        return self.items.pop(index)

    def __str__(self) -> str:
        return '\n'.join((str(self.title), '---', *(str(item) for item in self.items)))
