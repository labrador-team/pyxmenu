from pyxmenu.item import Item


class Divider(Item):
    """
    A divider item that will be rendered as a divider in the xbar menu.
    """
    def __init__(self):
        super().__init__(text='---')
