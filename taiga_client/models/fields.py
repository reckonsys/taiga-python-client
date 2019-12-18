from dataclasses import MISSING, Field as _Field


class Field(_Field):
    '''A custom field definition.'''

    def __init__(self, required=False, default=MISSING):
        if required is False and default is MISSING:
            default = None
        super(Field, self).__init__(
            default, default_factory=MISSING, init=True, repr=True, hash=None,
            compare=True, metadata=None)
