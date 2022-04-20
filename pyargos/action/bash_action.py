import typing

from pyargos.action.argos_action import ArgosAction
from pyargos.utils.format import format_bool_value


class BashAction(ArgosAction):
    def __init__(self, command: str, terminal: bool = False, params: typing.Iterable[str] = ()):
        """
        Initiates a bash action to run a command.

        Args:
            command: The command to run.
            terminal: Whether to open terminal windows which will run the command.
            params: The params to pass to the command.
        """

        self.command = command
        self.terminal = terminal
        self.params = params

    def __str__(self) -> str:
        params = [' param{index}={param}'.format(index=i + 1, param=param)
                  for i, param in enumerate(self.params)]
        params = ''.join(params) if params else ''

        return f'bash="{self.command}{params}" terminal={format_bool_value(self.terminal)}'
