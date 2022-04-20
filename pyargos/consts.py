import os

_ARGOS_SEPERATOR_STR = '---'
_NEW_LINE = '\n'

ARGOS_VERSION = os.environ.get('ARGOS_VERSION', os.environ.get('ARDOS_VERSION', 'Unknown'))
