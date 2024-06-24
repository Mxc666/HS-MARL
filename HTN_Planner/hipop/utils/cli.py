import argparse
import enum

def add_bool_arg(parser: argparse.ArgumentParser, name: str, dest: str, help: str, default: bool = False):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=dest,
                           help=(f"{help} (default)" if default else help),
                           action='store_true')
        group.add_argument('--no-' + name, dest=dest,
                           help=(f"do not {help}" if default 
                                 else f"do not {help} (default)"),
                           action='store_false')
        parser.set_defaults(**{dest: default})


class EnumAction(argparse.Action):
    """
    Argparse action for handling Enums
    """

    def __init__(self, **kwargs):
        # Pop off the type value
        e = kwargs.pop("type", None)
        # Ensure an Enum subclass is provided
        if e is None:
            raise ValueError(
                "type must be assigned an Enum when using EnumAction")
        if not issubclass(e, enum.Enum):
            raise TypeError("type must be an Enum when using EnumAction")
        # Generate choices from the Enum
        kwargs.setdefault("choices", tuple(x.value for x in e))
        super(EnumAction, self).__init__(**kwargs)
        self._enum = e

    def __call__(self, parser, namespace, values, option_string=None):
        # Convert value back into an Enum
        e = self._enum(values)
        setattr(namespace, self.dest, e)
