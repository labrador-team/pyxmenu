import base64
import os.path
import typing

from pyargos.argos_icon_object import ArgosIconObject

_DEFAULT_IMAGE_SIZE = 16


class ArgosImageIcon(ArgosIconObject):
    """
    Attributes:
        source: The icon source.
    """

    source: bytes
    width: int
    height: int

    def __init__(self, source: typing.Union[str, bytes], width: int = _DEFAULT_IMAGE_SIZE,
                 height: int = _DEFAULT_IMAGE_SIZE):
        if isinstance(source, str):
            source = source.encode()

        self.source = source
        self.width = width
        self.height = height

    def _load_image_from_source(self) -> str:
        """
        Loads the image from the source.
        The source can be the image data or a file path to an image.

        Returns:
            The image.
        """
        data = self.source

        if os.path.exists(self.source):
            with open(self.source, 'rb') as image_file:
                data = image_file.read()

        return base64.b64encode(data).decode()

    def __str__(self) -> str:
        return ' '.join((
            f'image="{self._load_image_from_source()}"',
            f'imageWidth={self.width}',
            f'imageHeight={self.height}'
        ))
