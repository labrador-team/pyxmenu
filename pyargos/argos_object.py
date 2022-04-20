from abc import ABCMeta


class ArgosObject(object):
    __metaclass__ = ABCMeta

    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return str(self)
