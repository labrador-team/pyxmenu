from pyargos.action.argos_action import ArgosAction


class RefreshAction(ArgosAction):
    def __str__(self) -> str:
        return 'refresh=true'
