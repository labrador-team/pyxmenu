from pyargos.action.argos_action import ArgosAction


class HrefAction(ArgosAction):
    def __init__(self, href: str):
        """
        Initiates a href action to open an url.

        Args:
            href: The href to open.
        """
        self.href = href

    def __str__(self) -> str:
        return 'href="{href}"'.format(href=self.href)
