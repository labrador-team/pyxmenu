from pyxmenu.item.attribute.__base__ import AttributeName, Attribute
from pyxmenu.item.attribute.alternative import AlternativeAttribute
from pyxmenu.item.attribute.ansi import AnsiAttribute
from pyxmenu.item.attribute.color import ColorAttribute
from pyxmenu.item.attribute.disabled import DisabledAttribute
from pyxmenu.item.attribute.dropdown import DropdownAttribute
from pyxmenu.item.attribute.emojize import EmojizeAttribute
from pyxmenu.item.attribute.font import FontAttribute
from pyxmenu.item.attribute.href import HrefAttribute
from pyxmenu.item.attribute.image import ImageAttribute
from pyxmenu.item.attribute.key import KeyAttribute
from pyxmenu.item.attribute.length import LengthAttribute
from pyxmenu.item.attribute.parmas import ParamsAttribute
from pyxmenu.item.attribute.refresh import RefreshAttribute
from pyxmenu.item.attribute.shell import ShellAttribute
from pyxmenu.item.attribute.size import SizeAttribute
from pyxmenu.item.attribute.template_image import TemplateImageAttribute
from pyxmenu.item.attribute.terminal import TerminalAttribute
from pyxmenu.item.attribute.trim import TrimAttribute

# All valid attributes that xbar can handle.
# New attributes should be added here.
ATTRIBUTES = [
    AnsiAttribute,
    AlternativeAttribute,
    ColorAttribute,
    DisabledAttribute,
    DropdownAttribute,
    EmojizeAttribute,
    FontAttribute,
    HrefAttribute,
    ImageAttribute,
    KeyAttribute,
    LengthAttribute,
    ParamsAttribute,
    RefreshAttribute,
    ShellAttribute,
    SizeAttribute,
    TemplateImageAttribute,
    TerminalAttribute,
    TrimAttribute,
]

ATTRIBUTES_MAPPING = {
    attribute.name: attribute
    for attribute in ATTRIBUTES
}
