"""The example from the readme."""
import tau
from tau.contracts import readable_file

tbar = tau.Tau(desc='Example Readme Interface.')


@tbar.command
@tau.argument(
    name='msg',
    contract='string',
    default='Hello World!',
    env_var='TAUDEMO_MSG',
    desc='Message to print',
)
def echo(msg):
    """Display a message on stdout."""
    print(msg)


math = tbar.group(name='math', desc='Utterly trivial math utilities.')

addable_arg = tau.argument(
    contract=lambda x: hasattr(x, '__add__'),
    desc='Number to add.')


@math.command
@addable_arg
@addable_arg
def add(x, y):
    """Add two numbers."""
    return x + y


@tbar.command
@tau.argument(
    name='fname',
    contract=readable_file,
    default='/etc/passwd',
    env_var='TAUDEMO_FILE',
    desc='Read the contents of a file on disk.',
)
@tau.option(
    name='loudly',
    contract='bool',
    desc='Read a file',
)
def cat(fname, loudly=False):
    """Read a file, quietly?"""
    with open(fname, 'r') as f:
        if loudly:
            return f.read().upper()
        else:
            return f.read()


cli = tbar.click()
app = tbar.flask()
