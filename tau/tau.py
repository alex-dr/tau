from __future__ import absolute_import
from functools import wraps

from tau.providers import *  # noqa


class Tau(object):
    """The main class for the tau library.

    A Tau is essentially a group of commands and their options, represented as
    an abstract interface, with methods on itself to create concrete interfaces
    from implemented providers.

    Example:

        >>> from tau import Tau
        >>> tbar = Tau()
        >>> @tbar.command
            def foo():
                pass
        >>> tbar.cli()
        <click.core.Group at 0x7f9cf5739f50>

    Providers are implementations of a simple interface for creating dynamic
    interfaces. In the example above, we create a Click Command-Line interface
    that is automatically generated from the Tau we created.

    Any number of providers may be generated from a single tau.  Continuing the
    above example:

        >>> tbar.flask().run()

    This invocation will create a fully-fledged Flask app and serve it with
    default Flask settings.
    """
    def __init__(self, desc=None):
        """Initialize the Tau.

        Parameters
        ----------
        desc : optional, str|None
            Description of this interface (for help messages etc).
        """
        self.commands = {}

        self.desc = desc

    def command(self, name=None):
        """Function decorator to create an interface command.

        An interface command is how we mark functions as Tau interface
        command or action to take.

        The command is added to the set of commands.

        Parameters
        ----------
        name : string|None
            Name of the command. Default is function name with _ > -
        """
        def decorator(fn):
            cmd_name = name or fn.__name__
            self.commands[cmd_name] = fn

            @wraps(fn)
            def wrapped(*args, **kwargs):
                fn(*args, **kwargs)
            return wrapped
        return decorator

    def argument(self, fn, **spec):
        """Function decorator to create a command argument."""
        @wraps(fn)
        def wrapped(*args, **kwargs):
            fn(*args, **kwargs)
        return wrapped

    def get_provider(self, name, *args, **kwargs):
        """Return provider instance."""
        module = __import__('tau.providers')
        klass = getattr(module.providers, name)
        return klass(self, *args, **kwargs)
