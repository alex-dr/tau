"""Tau primary module.

You probably want to do this:

    >>> from tau import Tau
"""
from __future__ import absolute_import
from functools import wraps

from .providers import *  # noqa


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
        >>> tbar.click()
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
        self.commands = []

        self.desc = desc

    def command(self, fn):
        """Function decorator to create an interface command.

        An interface command is how we mark functions as Tau interface
        command or action to take.

        The command is added to the set of commands.
        """
        self.commands.append(fn)

        @wraps
        def wrapped(*args, **kwargs):
            fn(*args, **kwargs)
        return wrapped

    def argument(self, fn, **spec):
        """Function decorator to create a command argument.
        """
        @wraps
        def wrapped(*args, **kwargs):
            fn(*args, **kwargs)
        return wrapped

    def __getattr__(self, name):
        """Return provider classes as attributes.

        This enables the following usage.

            >>> import tau
            >>> t = tau.Tau(foo='bar')
            >>> t.abstract()

        """
        try:
            mod = __import__('tau.providers')
            return getattr(mod, name)
        except (ImportError, AttributeError):
            return self.__getattribute__(name)
