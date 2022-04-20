from pyargos.argos_icon_object import ArgosIconObject


class ArgosIcon(ArgosIconObject):
    """
    Attributes:
        icon_name: The icon name.
    """

    icon_name: str

    def __init__(self, icon_name: str):
        """
        Args:
            icon_name: The icon name.
        """
        self.icon_name = icon_name

    def __str__(self) -> str:
        return f'iconName={self.icon_name}'
