from __future__ import absolute_import
from functools import wraps

import contracts

from contracts.interface import ContractNotRespected

from tau.errors import SpecValidationError
from tau.providers import *  # noqa

# Load up handy named contracts
import tau.common_contracts  # noqa


class Tau(object):
    """The main class for the tau library.

    A Tau is essentially a group of commands and their options, represented as
    an abstract interface, with methods on itself to create concrete interfaces
    from implemented providers.

    Example:

        >>> from tau import Tau
        >>> tbar = Tau()
        >>> @tbar.command()
            def foo():
                pass
        >>> tbar.get_provider('cli')
        <tau.providers.cli.ClickProvider at 0x7f9cf5739f50>

    Providers are implementations of a simple interface for creating dynamic
    interfaces. In the example above, we create a Click Command-Line interface
    that is automatically generated from the Tau we created.

    Any number of providers may be generated from a single tau.  Continuing the
    above example:

        >>> tbar.flask().run()

    This invocation will create a fully-fledged Flask app and serve it with
    default Flask settings.
    """

    commands = {}

    def __init__(self, desc=None):
        """Initialize the Tau.

        Parameters
        ----------
        desc : optional, str|None
            Description of this interface (for help messages etc).
        """
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
                return fn(*args, **kwargs)
            return wrapped
        return decorator

    def get_provider(self, name, *args, **kwargs):
        """Return provider instance."""
        module = __import__('tau.providers')
        klass = getattr(module.providers, name)
        return klass(self, *args, **kwargs)


def argument(name, **spec):
    """Function decorator to create a command argument."""
    _validate_argspec(spec)

    def decorator(fn):
        if hasattr(fn, '__tau_args__'):
            fn.__tau_args__[name] = spec
        else:
            fn.__tau_args__ = {name: spec}

        @wraps(fn)
        def wrapped(*args, **kwargs):
            # TODO
            # If there is a default and we are called without it,
            # figure out how to set the value here, be it an arg or kwarg.
            return fn(*args, **kwargs)
        return wrapped
    return decorator


# Allowed parameters for tau.argument
# Arguments are used to provide naming, validation, and documentation to
# command parameters.
# They can also provide additional configuration that is recognized only
# by particular providers, for example you might want to prompt for user input
# on a CLI argument, but there is no comparable operation for REST API's.
ARG_SCHEMA = {
    'desc': {
        'desc': 'Short description for your argument.',
        'contract': 'tau_desc',
    },
    'short': {
        'desc': 'One-character identifier for your argument.',
        'contract': 'tau_single_char',
    },
    'contract': {
        'desc': 'Contract to execute when validating this function.',
        'contract': 'string',
        'default': '*',
    },
    'config_key': {
        'desc': 'Key to look up in config file.',
        'contract': 'string|None',
    },
    'env_var': {
        'desc': 'Environment variable to look up.',
        'contract': 'string|None',
    },
    'optional': {
        'desc': 'Whether this arg is optional.',
        'contract': 'bool',
        'default': False,
    },
    'default': {
        'desc': 'Lowest priority default for an argument.',
        'contract': '*',
    },
}


def _validate_argspec(spec):
    """Ensure user's argument is properly formed."""
    for key, value in spec.items():
        # Explicitly allow extra keys
        contract = ARG_SCHEMA.get(key, {}).get('contract', '*')
        try:
            contracts.check(contract, value)
        except ContractNotRespected as exc:
            raise SpecValidationError(exc.name, exc, desc=value['desc'])
