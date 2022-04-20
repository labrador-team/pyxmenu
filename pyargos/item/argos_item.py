import typing

from pyargos.action.argos_action import ArgosAction
from pyargos.action.refresh_action import RefreshAction
from pyargos.argos_icon_object import ArgosIconObject
from pyargos.argos_object import ArgosObject
from pyargos.consts import _NEW_LINE
from pyargos.utils.format import format_bool_value


class ArgosItem(ArgosObject):
    """
    Attributes:
        text: The text of the item.
        icon: The icon of the item.
        action: The action to run when the item is clicked.
        refresh: Whether to refresh the plugin when the item is clicked.
        color: The color of the item's text.
        font_family: The font to use for the item's text.
        font_size: The size of the item's text.
        length: The length at which to truncate the text. 0 for no truncation.
        trim: Whether to trim whitespaces at the start and end of the text.
        dropdown: Whether the item is a dropdown item.
        alternative: An alternative item to view when the ALT key is held. None for no alternative
                     item.
        emojize: Whether to show emojis in the text.
        ansi: Whether to support ansi in the text.
        use_markup: Whether to use markup in the text.
        unescape: Whether to unescape special characters in the text.
    """

    text: str
    icon: typing.Optional[ArgosIconObject] = None
    action: typing.Optional[ArgosAction] = None
    refresh: bool = False
    color: typing.Optional[str] = None
    font_family: str = 'Segoe UI'
    font_size: int = 9
    length: int = 0
    trim: bool = True
    dropdown: bool = True
    alternative: typing.Optional['ArgosItem'] = None
    emojize: bool = True
    ansi: bool = True
    use_markup: bool = True
    unescape: bool = True

    def __init__(self,
                 text: str,
                 icon: typing.Optional[ArgosIconObject] = None,
                 action: typing.Optional[ArgosAction] = None,
                 refresh: bool = False,
                 color: typing.Optional[str] = None,
                 font_family: str = 'Segoe UI',
                 font_size: int = 9,
                 length: int = 0,
                 trim: bool = True,
                 dropdown: bool = True,
                 alternative: typing.Optional['ArgosItem'] = None,
                 emojize: bool = True,
                 ansi: bool = True,
                 use_markup: bool = True,
                 unescape: bool = True
                 ):
        """
        Args:
            text: The text of the item.
            icon: The icon of the item.
            action: The action to run when the item is clicked.
            refresh: Whether to refresh the plugin when the item is clicked.
            color: The color of the item's text.
            font_family: The font to use for the item's text.
            font_size: The size of the item's text.
            length: The length at which to truncate the text. 0 for no truncation.
            trim: Whether to trim whitespaces at the start and end of the text.
            dropdown: Whether the item is a dropdown item.
            alternative: An alternative item to view when the ALT key is held. None for no
                         alternative item.
            emojize: Whether to show emojis in the text.
            ansi: Whether to support ansi in the text.
            use_markup: Whether to use markup in the text.
            unescape: Whether to unescape special characters in the text.
        """
        self.text = text
        self.icon = icon
        self.action = action
        self.refresh = refresh
        self.color = color
        self.font_family = font_family
        self.font_size = font_size
        self.length = length
        self.trim = trim
        self.dropdown = dropdown
        self.alternative = alternative
        self.emojize = emojize
        self.ansi = ansi
        self.use_markup = use_markup
        self.unescape = unescape

    def __str__(self) -> str:
        attributes = []

        if self.icon:
            attributes.append(str(self.icon))

        if self.action:
            attributes.append(str(self.action))

        if self.refresh:
            attributes.append((str(RefreshAction())))

        if self.color:
            attributes.append(f'color="{self.color}"')

        if self.font_family:
            attributes.append(f'font="{self.font_family}"')

        if self.font_size:
            attributes.append(f'size={self.font_size}')

        if self.length:
            attributes.append(f'length={self.length}')

        attributes.append(f'trim={format_bool_value(self.trim)}')

        attributes.append(f'dropdown={format_bool_value(self.dropdown)}')

        if self.alternative:
            attributes.append(f'alternate=true')

        attributes.append(f'emojize={format_bool_value(self.emojize)}')

        attributes.append(f'ansi={format_bool_value(self.ansi)}')

        attributes.append(f'useMarkup={format_bool_value(self.use_markup)}')

        attributes.append(f'unescape={format_bool_value(self.unescape)}')

        string = self.text

        if attributes:
            string += f' | {" ".join(attributes)}'

        if self.alternative:
            string += f'{_NEW_LINE}{self.alternative}'

        return string
