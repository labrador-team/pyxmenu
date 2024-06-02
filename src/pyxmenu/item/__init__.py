import inspect
from typing import Optional, TypeVar

from pyxmenu.item.attribute import ATTRIBUTES_MAPPING
from pyxmenu.item.attribute.__base__ import AttributeName, Attribute, INVALID_ATTRIBUTE_VALUE

TItem = TypeVar("TItem", bound="Item")


class Item:
    """
    A representation of an x-bar item.

    Attributes:
        text: The text that is displayed.
        attributes: The attributes of the item.
        children: The children of the item.

    Notes:
        This class uses the builder pattern to specify the children.
    """
    text: str
    attributes: dict[AttributeName, Attribute]
    children: list['Item']

    _nesting_level: int

    def __init__(
            self,
            text: str,
            children: Optional[list['Item']] = None,
            *,
            key: Optional[str] = None,
            href: Optional[str] = None,
            color: Optional[str] = None,
            font: Optional[str] = None,
            size: Optional[int] = None,
            shell: Optional[str] = None,
            params: Optional[list[str] | str] = None,
            terminal: Optional[bool] = None,
            refresh: Optional[bool] = None,
            dropdown: Optional[bool] = None,
            length: Optional[int] = None,
            trim: Optional[bool] = None,
            alternative: Optional['Item'] = None,
            template_image: Optional[str] = None,
            image: Optional[str] = None,
            emojize: Optional[bool] = None,
            ansi: Optional[bool] = None,
            disabled: Optional[bool] = None,
    ):
        """
        Initialize the item with the given parameters.

        Args:
            text: The text that is displayed.
            children: The children to add to the item.
            key: A keyboard shortcut to trigger the item.
            href: The URL to open when the item is triggered.
            color: The color of the text, can be color name or hex.
            font: The font of the text.
            size: The size of the text.
            shell: The shell command to execute when the item is triggered.
            params: The parameters to pass to the shell command. The params can be a list or a comma separated string.
            terminal: Whether to show the shell execution in a terminal window.
            refresh: Whether to refresh the plugin when it is triggered. This is disabled by default.
            dropdown: Whether to show the item in the dropdown or just the status bar.
            length: The length of the text. If the text is longer it will be truncated with "...".
            trim: Whether to trim the text. This is enabled by default.
            alternative: An alternative item to show when the Option key is pressed.
            template_image: The template image to use. The image must be a base64 encoded string and should consist of
                            only black and clear pixels. The alpha channel in the image can be used to adjust the
                            opacity of black content, however. This is the recommended way (by xbar) to set the image
                            for the status bar. Use a 144 DPI resolution to support Retina displays. The image format
                            can be any of the formats supported by Mac OS X
            image: The image to use. The image must be a base64 encoded string. Use a 144 DPI resolution to support
                   Retina displays. The image format can be any of the formats supported by Mac OS X.
            emojize: Whether to emojize the text (i.e. :mushroom: will be translated to 🍄). This is enabled by default.
            ansi: Whether to parse ANSI color codes in the text. This is enabled by default.
            disabled: Whether to disable the item. This is disabled by default.
        """
        self.text = text
        self.attributes = {}
        self.children = []
        self._nesting_level = 0

        if children is not None:
            self.add_children(children)

        kwargs = dict(zip(inspect.getfullargspec(Item.__init__).kwonlyargs, [
            key,
            href,
            color,
            font,
            size,
            shell,
            params,
            terminal,
            refresh,
            dropdown,
            length,
            trim,
            alternative,
            template_image,
            image,
            emojize,
            ansi,
            disabled
        ]))

        for key, value in kwargs.items():
            if value is None:
                continue

            attribute_class = ATTRIBUTES_MAPPING.get(AttributeName(key))

            if attribute_class is None:
                continue

            self.attributes[attribute_class.name] = attribute_class(value)

    def add_child(self: TItem, child: 'Item', index: Optional[int] = None) -> TItem:
        """
        Add a child to the item.

        Args:
            child: The child to add.
            index: The index to add the child at. If None, the child will be added at the end.

        Returns:
            The item itself.
        """
        child._set_nested_of(self)

        if index is not None:
            self.children.insert(index, child)
        else:
            self.children.append(child)

        return self

    def add_children(self: TItem, children: list['Item'], index: Optional[int] = None) -> TItem:
        """
        Add children to the item.

        Args:
            children: The children to add.
            index: The index to add the children at. If None, the children will be added at the end.

        Returns:
            The item itself.
        """
        for child in children:
            child._set_nested_of(self)

        if index is not None:
            self.children[index:index] = children
        else:
            self.children.extend(children)

        return self

    def remove_child(self: TItem, child: 'Item') -> TItem:
        """
        Remove a child from the item.

        Args:
            child: The child to remove.

        Returns:
            The item itself.
        """
        self.children.remove(child)
        return self

    def remove_children(self: TItem, children: list['Item']) -> TItem:
        """
        Remove children from the item.

        Args:
            children: The children to remove.

        Returns:
            The item itself.
        """
        for child in children:
            self.children.remove(child)

        return self

    def pop_child(self: TItem, index: int) -> 'Item':
        """
        Remove a child from the item and return it.

        Args:
            index: The index of the child to remove.

        Returns:
            The removed child.
        """
        return self.children.pop(index)

    def _set_nesting_level(self: TItem, nesting_level: int):
        """
        Set the nesting level of the item and its children.

        Args:
            nesting_level: The nesting level to set.
        """
        self._nesting_level = nesting_level

        for child in self.children:
            child._set_nesting_level(nesting_level + 1)

    def _set_nested_of(self: TItem, item: 'Item'):
        """
        Set the nesting level of the item and its children based on the given item.

        Args:
            item: The item to set the base nesting level from.

        """
        self._set_nesting_level(item._nesting_level + 1)

    def __str__(self: TItem) -> str:
        text = self.text

        if self._nesting_level > 0:
            text = f'{"--" * self._nesting_level}{text}'

        if len(self.attributes) > 0:
            parsed_attributes = ' '.join(
                str(item_attribute)
                for item_attribute in self.attributes.values()
                if item_attribute.value != INVALID_ATTRIBUTE_VALUE and item_attribute.name != AttributeName.ALTERNATIVE
            )

            text += f' | {parsed_attributes}'

        if ((alternative := self.attributes.get(AttributeName.ALTERNATIVE)) is not None
                and self.attributes.get(AttributeName.KEY) is None):
            text += str(alternative)

        if len(self.children) > 0:
            text += '\n' + '\n'.join(str(child) for child in self.children)

        return text
