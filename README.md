# pyxmenu

![PyPI](https://img.shields.io/pypi/v/pyxmenu?label=pypi%20package)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyxmenu)

`pyxmenu` is a Python library for helping you create python plugins for [xbar](https://xbarapp.com), 
[argos](https://github.com/p-e-w/argos) and [ardos](https://github.com/labrador-team/ardos) with ease!

The library wraps all the menu creation logic with classes and objects to let you create a plugin with a few lines of 
code and without dealing with string formatting complications.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyxmenu.

```bash
pip install pyxmenu
```

## Usage

```python
from pyxmenu import Plugin, Item

# Create a new xbar plugin
plugin = Plugin(
    # Set the title of the plugin
    title=Item("My Plugin", font="Menlo", size=20),
    # Add items to the plugin
    items=[
        Item("Hello", color="blue", href="https://github.com/labrador-team/pyxmenu")
    ]
).add_items(
    # Add multiple items to the plugin
    [
        Item("World", color="red", key="shift+k"),
        Item("Foo", color="green", alternative=Item("Bar", color="yellow")),
        # Add item with submenu
        Item("Baz", color="purple", children=[
            Item("Qux"),
            Item("Quux"),
        ]),
    ]
)

print(plugin)
```

## Contributing

Please open an issue first to discuss what you would like to change.
We welcome any and all criticism, feedback, and suggestions even if we may not agree.
