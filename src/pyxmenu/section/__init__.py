from typing import Optional, TypeVar

from pyxmenu import Item

TSection = TypeVar('TSection', bound='Section')


class Section:
    """
    An x-bar section of items.

    A section is a group of items that are separated by a line above and bellow.

    Attributes:
        items: The items of the section.
    """
    items: list[Item]

    def __init__(self, *items: Item):
        self.items = list(items)

    def add_item(self: TSection, item: Item, index: Optional[int] = None) -> TSection:
        """
        Add an item to the section.

        Args:
            item: The item to add.
            index: The index to add the item at. If None, the item will be added at the end.

        Returns:
            The section itself.
        """
        if index is not None:
            self.items.insert(index, item)
        else:
            self.items.append(item)

        return self

    def add_items(self: TSection, items: list[Item], index: Optional[int] = None) -> TSection:
        """
        Add multiple items to the section.

        Args:
            items: The items to add.
            index: The index to add the items at. If None, the items will be added at the end.

        Returns:
            The section itself.
        """
        if index is not None:
            self.items[index:index] = items
        else:
            self.items.extend(items)

        return self

    def remove_item(self: TSection, item: Item) -> TSection:
        """
        Remove an item from the section.

        Args:
            item: The item to remove.

        Returns:
            The section itself.
        """
        self.items.remove(item)
        return self

    def pop_item(self: TSection, index: int) -> Item:
        """
        Pop an item from the section.

        Args:
            index: The index of the item to pop.

        Returns:
            The popped item.
        """
        return self.items.pop(index)

    def __str__(self):
        return '\n'.join(('---', *(str(item) for item in self.items), '---'))
