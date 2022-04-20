import typing

from pyargos.argos_object import ArgosObject
from pyargos.consts import _ARGOS_SEPERATOR_STR, _NEW_LINE
from pyargos.item.argos_item import ArgosItem


class ArgosPlugin(ArgosObject):
    """
    Attributes:
        item: The item to represent the plugin with.
        plugin_items: The items of the plugin.
    """

    item: ArgosItem
    plugin_items = typing.Iterable[ArgosItem]

    def __init__(self, item: ArgosItem, plugin_items: typing.Iterable[ArgosItem]):
        """
        Initiates an Argos plugin.

        Args:
            item: The item to represent the plugin with.
            plugin_items: The items of the plugin.
        """
        self.item = item
        self.plugin_items = plugin_items

    def __str__(self):
        return _NEW_LINE.join((
            str(self.item),
            _ARGOS_SEPERATOR_STR,
            *(str(item) for item in self.plugin_items)
        ))

    def run(self):
        string = str(self)
        string = string.replace(f'{_ARGOS_SEPERATOR_STR}{_NEW_LINE}{_ARGOS_SEPERATOR_STR}',
                                _ARGOS_SEPERATOR_STR)

        print(string)
